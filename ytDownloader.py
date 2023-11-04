# Create virtual enviroment
# python -m venv venvYD
# venvYD\Scripts\activate

from pytube import YouTube
from sys import argv

#link = argv[1]
link = 'https://www.youtube.com/watch?v=LDU_Txk06tM'
yt = YouTube(link)
quality = 'get_lowest_resolution()'
downloadFolder = 'E:\YT Downloads'



print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_lowest_resolution()

yd.download(downloadFolder)