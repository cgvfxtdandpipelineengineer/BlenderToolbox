import sys

import logging

if sys.version_info.major == 2:
    from pathlib2 import Path
elif sys.version_info.major == 3:
    from pathlib import Path
else:
    raise RuntimeError("This script is only supported on Python 2 and 3")

if sys.version_info.major == 2:
    from urllib2 import urlopen
elif sys.version_info.major == 3:
    from urllib.request import urlopen
else:
    raise RuntimeError("This script is only supported on Python 2 and 3")

from bs4 import BeautifulSoup

import zipfile


logger = logging.getLogger(__name__)


class DestinationPathAlreadyExists(RuntimeError):
    pass


class DownloadError(RuntimeError):
    pass


class ArchiveExtractionError(RuntimeError):
    pass


class DownloadSource(object):
    def __init__(self, download_path):
        self.download_path = download_path
        self.page = None
    
    def prepare(self):
        self.page = urlopen(self.download_path)
    
    def get_files(self):
        files_to_download = []

        soup = BeautifulSoup(self.page, 'html.parser')
        tables = soup.findAll('table', attrs={'class': 'table table-striped table-hover box'})
        
        logging.warning("Scraping links for downloadable archive files")
        
        for table in tables:
            anchors = table.findAll('a')
            for anchor in anchors:
                download_link = self.download_path + '/' + anchor.text
                files_to_download.append((anchor.text, download_link))
        
        return files_to_download

    @classmethod
    def downloadURL(cls, url, destination_path):
        opened_url = urlopen(url)

        logger.warning("Downloading to {0}".format(destination_path))

        with open(str(destination_path), 'wb') as output:
            output.write(opened_url.read())


class DownloadDestination(object):
    def __init__(self, download_path):
        self.path = Path(download_path).expanduser()

    def prepare(self):
        self._create_download_path()

    def _create_download_path(self):
        if not self.path.exists():
            self.path.mkdir(parents=True)
    
    def extract_zip(self, zipfilepath):
        try:
            zipped = zipfile.ZipFile(str(zipfilepath))
            logger.warning("Extracting {0}".format(str(zipfilepath)))
            zipped.extractall(path=str(zipfilepath.parent))
            logging.info("Extracted zip file {0}".format(zipfilepath))
        except Exception as e:
            raise ArchiveExtractionError(e) 


class DownloadManager(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def prepare(self):
        self.source.prepare()
        self.destination.prepare()
    
    def download_file(self, filename, url):
        destination_path = self.destination.path / filename

        if destination_path.exists():
            message = "Path already exists {0}".format(destination_path)
            raise DestinationPathAlreadyExists(message)

        try:
            self.source.downloadURL(url, destination_path)
        except Exception as e:
            raise DownloadError(e)
        
        return destination_path

    def download(self):
        files = self.source.get_files()
        downloaded_paths = []
        for filename, url in files:
            try:
                downloaded_path = self.download_file(filename, url)
                downloaded_paths.append(downloaded_path)
            except DestinationPathAlreadyExists as e:
                logger.warning(e)
            except DownloadError as e:
                logger.warning(e)


if __name__ == '__main__':
    download_source = DownloadSource("https://builder.blender.org/download")
    download_destination = DownloadDestination('~/Downloads/Blender/BlenderToolbox/files')
    
    download_manager = DownloadManager(download_source, download_destination)
    
    download_manager.prepare()
    
    files = download_manager.source.get_files()
    
    #destination_path = download_manager.download_file(*files[1])
    #download_manager.destination.extract_zip(destination_path)
    #download_manager.download()
