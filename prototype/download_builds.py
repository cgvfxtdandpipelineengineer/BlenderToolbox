import pathlib2
import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


class DownloadSource(object):
    def __init__(self, download_path):
        self.download_path = download_path
        self.page = None
    
    def prepare(self):
        self.page = urllib2.urlopen(self.download_path)
    
    def get_files(self):
        files_to_download = []

        soup = BeautifulSoup(self.page, 'html.parser')
        tables = soup.findAll('table', attrs={'class': 'table table-striped table-hover box'})
        
        for table in tables:
            anchors = table.findAll('a')
            for anchor in anchors:
                download_link = self.download_path + '/' + anchor.text
                files_to_download.append((anchor.text, download_link))
        
        return files_to_download

    @classmethod
    def downloadURL(cls, url, destination_path):
        opened_url = urllib2.urlopen(url)

        print "Downloading to {0}".format(destination_path)

        with open(str(destination_path), 'wb') as output:
            output.write(opened_url.read())


class DownloadDestination(object):
    def __init__(self, download_path):
        self.path = pathlib2.Path(download_path).expanduser()

    def prepare(self):
        self._create_download_path()

    def _create_download_path(self):
        if not self.path.exists():
            self.path.mkdir()

    
class DownloadManager(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    
    def prepare(self):
        self.source.prepare()
        self.destination.prepare()
    
    def download(self):
        files = self.source.get_files()

        for filename, url in files:
            destination_path = self.destination.path / filename
            if destination_path.exists():
                print "Path already exists {0}".format(destination_path)
                continue
    
            self.source.downloadURL(url, destination_path)

if __name__ == '__main__':
    download_source = DownloadSource("https://builder.blender.org/download")
    download_destination = DownloadDestination('~/Downloads/Blender/BlenderToolbox/files')
    
    download_manager = DownloadManager(download_source, download_destination)
    
    download_manager.prepare()
    
    download_manager.download()
