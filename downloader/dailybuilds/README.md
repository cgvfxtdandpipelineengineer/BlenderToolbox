```python
In [2]: (executing lines 1 to 126 of "downloader_dailybuilds.py")
Scraping links for downloadable archive files

In [3]: files
Out[3]: 
[(u'blender-2.79-b99d064-win64.zip',
  u'https://builder.blender.org/download/blender-2.79-b99d064-win64.zip'),
 (u'blender-2.79-c84b8d4-win64-vc14.zip',
  u'https://builder.blender.org/download/blender-2.79-c84b8d4-win64-vc14.zip'),
 (u'blender-2.80-9c21239-win64.zip',
  u'https://builder.blender.org/download/blender-2.80-9c21239-win64.zip'),
 (u'blender-2.80-6c6a394-win64-vc14.zip',
  u'https://builder.blender.org/download/blender-2.80-6c6a394-win64-vc14.zip'),
 (u'blender-2.79-b99d064-win32.zip',
  u'https://builder.blender.org/download/blender-2.79-b99d064-win32.zip'),
 (u'blender-2.80-a0c564f-win32.zip',
  u'https://builder.blender.org/download/blender-2.80-a0c564f-win32.zip'),
 (u'blender-2.79-b99d064e914-linux-glibc219-x86_64.tar.bz2',
  u'https://builder.blender.org/download/blender-2.79-b99d064e914-linux-glibc219-x86_64.tar.bz2'),
 (u'blender-2.80-a0c564f86aa-linux-glibc219-x86_64.tar.bz2',
  u'https://builder.blender.org/download/blender-2.80-a0c564f86aa-linux-glibc219-x86_64.tar.bz2'),
 (u'blender-2.79-c84b8d48019-linux-glibc219-i686.tar.bz2',
  u'https://builder.blender.org/download/blender-2.79-c84b8d48019-linux-glibc219-i686.tar.bz2'),
 (u'blender-2.80-9c212399c6d-linux-glibc219-i686.tar.bz2',
  u'https://builder.blender.org/download/blender-2.80-9c212399c6d-linux-glibc219-i686.tar.bz2'),
 (u'blender-2.79-b99d064e914-OSX-10.9-x86_64.zip',
  u'https://builder.blender.org/download/blender-2.79-b99d064e914-OSX-10.9-x86_64.zip'),
 (u'blender-2.80-a0c564f86aa-OSX-10.9-x86_64.zip',
  u'https://builder.blender.org/download/blender-2.80-a0c564f86aa-OSX-10.9-x86_64.zip')]

In [4]: destination_path = download_manager.download_file(*files[1])
Downloading to C:\Users\sgoda\Downloads\Blender\BlenderToolbox\files\blender-2.79-c84b8d4-win64-vc14.zip

In [5]: download_manager.destination.extract_zip(destination_path)
Extracting C:\Users\sgoda\Downloads\Blender\BlenderToolbox\files\blender-2.79-c84b8d4-win64-vc14.zip

In [6]: destination_path = download_manager.download_file(*files[3])
Downloading to C:\Users\sgoda\Downloads\Blender\BlenderToolbox\files\blender-2.80-6c6a394-win64-vc14.zip

In [7]: download_manager.destination.extract_zip(destination_path)
Extracting C:\Users\sgoda\Downloads\Blender\BlenderToolbox\files\blender-2.80-6c6a394-win64-vc14.zip

```
