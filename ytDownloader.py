# Create virtual enviroment
# python -m venv ytdown
# ytdown\Scripts\activate

from pytube import YouTube
from sys import argv

#link = argv[1]
yt = YouTube('https://www.youtube.com/watch?v=kCMJxOSiWrg')

print("Title: ", yt.title)
print("View: ", yt.views)