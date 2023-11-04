# Create virtual enviroment
# python -m venv venvYD
# venvYD\Scripts\activate
# https://github.com/israel-dryer/ttkbootstrap/issues/505 - Changed local from "" to "nb_NO.utf8"

#ttkbootstrap

import tkinter as tk
import ttkbootstrap as tb
import locale

from ttkbootstrap.constants import *
from tkinter import messagebox
from pytube import YouTube
from sys import argv


locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
#link = argv[1]
#link = 'https://www.youtube.com/watch?v=LDU_Txk06tM'
#link = ""
#yt = YouTube(link)
quality = 'get_lowest_resolution()'
downloadFolder = 'E:\YT Downloads'


#print("Title: ", yt.title)
#print("View: ", yt.views)
#print("Author: ", yt.author)


#yd = yt.streams.get_lowest_resolution()

#yd.download(downloadFolder)

# Button Commands
def close_function():
    root.destroy()

def download_function():
    messagebox.showinfo("Download", "Download button pressed")

def getInfo_function():
    try:
        link = url_entry.get()
        yt = YouTube(link)
        print("Title: ", yt.title)
        print("View: ", yt.views)
        print("Author: ", yt.author)
        title_label = tb.Label(text=("Title: " + yt.title))
        title_label.pack(pady=15)
        views_label = tb.Label(text=("Views: " + str(yt.views)))
        views_label.pack(pady=15)
        author_label = tb.Label(text=("Author: " + yt.author))
        author_label.pack(pady=15)
#        text1.insert(tk.END, "Title: " + yt.title)
#        text2.insert(tk.END, "Views: " + str(yt.views))
#        text3.insert(tk.END, "Author: " + yt.author)
    except Exception:
        print("Wrong data input")
#        text1.insert(tk.END, "WRONG URL INPUT")


# ------------------ #
root = tb.Window(themename="superhero")

root.title("YouTube Downloader")

welcome_label = tb.Label(text="Welcom to Youtube Downloader! Take a look around", font=("Helvetica", 18))
welcome_label.pack(pady=30)

url_entry = tb.Entry(root)
url_entry.pack(pady=15)

close_button = tb.Button(root, text="Close", bootstyle="danger-outline", command=close_function)
close_button.pack(pady=5)

getInfo_button = tb.Button(root, text="Get Info", bootstyle="info-outline", command=getInfo_function)
getInfo_button.pack(pady=5)

download_button = tb.Button(root, text="Download", bootstyle="success-outline", command=download_function)
download_button.pack(pady=5)



root.mainloop()