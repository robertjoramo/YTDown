# Requirements:
# pytube, Pillow, 

import tkinter as tk
import os
import urllib.request

from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
from pytube import YouTube
from PIL import ImageTk,Image

# ------ Functions ------ #

def progress_function(stream, chunk, reminder):
    current = ((stream.filesize - reminder)/stream.filesize)
    shortCurrent = ("%.3f" % float(current))
    p = (float(shortCurrent)*100)
    output = str(p) + '%'
    progress_lbl.config(text=output)
    progress_lbl.update()

def update_progress(progress):
    progress_label.set(progress)

def complete_func(stream, path):
    progress_lbl.config(text="Download Finished")


def folder_function():
    selectFolder = filedialog.askdirectory()
    local_folder.set(selectFolder)

def download_function():
    progress_lbl.config(text="Initiating ...")
    progress_lbl.update()

    try:
        if not os.path.isdir(local_folder.get()):
            raise Exception('No local folder selected')
   
        yd_quality = ""
        link = url_entry.get()
        yt = YouTube(link, on_progress_callback = progress_function, on_complete_callback=complete_func)

        quality_cehck = str(quality_var.get())
        match quality_cehck:
            case "1":
                yd_quality = yt.streams.filter(res="360p").first()
            case "2":
                yd_quality = yt.streams.filter(res="720p").first()
            case "3":
                yd_quality = yt.streams.filter(res="1080p").first()
            case "4":
                yd_quality = yt.streams.get_highest_resolution()

        if yd_quality is None:
            raise Exception('Selected Quality not available.')
        

        yt_title.set("Title: " + yt.title)
        yt_views.set("Views: " + str(yt.views))
        yt_channel.set("Channel: " + yt.author)

        yd_quality.download(output_path=local_folder.get())
        
    except Exception as inst:
        progress_lbl.config(text="Error")
        if inst:
            messagebox.showerror("Error", inst)
        else:
            messagebox.showerror("Error", "Not able to download, please try again")

def getInfo_function():
    try:
        link = url_entry.get()
        yt = YouTube(link)

        yt_title.set("Title: " + yt.title)
        yt_views.set("Views: " + str(yt.views))
        yt_channel.set("Channel: " + yt.author)

        load_thumbnail(yt.thumbnail_url)

    except Exception:
        print("Wrong data input")
        messagebox.showinfo("ERROR", "URL Error. Please enter another URL")

def load_thumbnail(url):
    urllib.request.urlretrieve(url, "thumbnail_url")
    img = Image.open("thumbnail_url")
    new_height = 150
    new_width = int(new_height / img.height * img.width)
    thumbnail = img.resize((new_width, new_height))
    img_thumbnail = ImageTk.PhotoImage(thumbnail)
    thumbnail_lbl.configure(image=img_thumbnail)
    thumbnail_lbl.image = img_thumbnail

def clear_labels():
    yt_title.set("")
    yt_views.set("")
    yt_channel.set("")
    thumbnail_lbl.image=""

# ------ Window ------ #
window=Tk()
window.title('Simply YT Downloader')
window.geometry("500x400")

# ------ Style ------ #
style = ttk.Style(window)
# style.theme_use("default")
# See included styles
# print(ttk.Style().theme_names()) # GIVES: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

# Custom Styling
style.configure('TButton',
              padding=[2])
style.configure('TEntry',
              padding=[4])
style.configure('TLabel',
              padding=[2])

# ------ Variables ------ #    
quality_var = IntVar(value=4)
local_folder = StringVar(value=os.getcwd())
progress_label = StringVar()
yt_title = StringVar()
yt_views = StringVar()
yt_channel = StringVar()

global progress_lbl

# ------ Widget ------ #
top_frame = ttk.Frame(window)
url_lbl = ttk.Label(top_frame, text = "Youtube URL: ")
url_entry = ttk.Entry(top_frame, width=60)

second_frame = ttk.Frame(window)
R_480p = ttk.Radiobutton(second_frame, text="360P", variable=quality_var, value=1)
R_720p = ttk.Radiobutton(second_frame, text="720P", variable=quality_var, value=2)
R_1080p = ttk.Radiobutton(second_frame, text="1080P", variable=quality_var, value=3)
R_highest = ttk.Radiobutton(second_frame, text="Highest", variable=quality_var, value=4)

third_frame = ttk.Frame(window)
lclFolder_lbl = ttk.Label(third_frame, textvariable=local_folder)
folder_btn = ttk.Button(third_frame, text = "Select Folder", command=folder_function)
progress_lbl = ttk.Label(third_frame, text = "")

fourth_frame = ttk.Frame(window)
getInfo_btn = ttk.Button(fourth_frame, text = "Get Info", command=getInfo_function)
download_btn = ttk.Button(fourth_frame, text = "Download", command=download_function)

fifth_frame = ttk.Frame(window)
title_label = ttk.Label(fifth_frame, textvariable = yt_title)
views_label = ttk.Label(fifth_frame, textvariable = yt_views)
channel_label = ttk.Label(fifth_frame, textvariable = yt_channel)
thumbnail_lbl = ttk.Label(fifth_frame, image="")

bottom_frame = ttk.Frame(window)


# ------ Layout ------ #
top_frame.pack(pady = (20,0), padx = 10,  fill=X)
url_lbl.pack(side = LEFT)
url_entry.pack(side = LEFT)

second_frame.pack(pady = (5,5), padx = 10)
R_480p.pack(side = LEFT)
R_720p.pack(side = LEFT)
R_1080p.pack(side = LEFT)
R_highest.pack(side = LEFT)

third_frame.pack(pady = 5,  fill=X, padx = 10)
folder_btn.pack(side = LEFT) 
lclFolder_lbl.pack(side = LEFT, padx = 10)
progress_lbl.pack(side = RIGHT, padx = 25)

fourth_frame.pack(pady = 5,  fill=X, padx = 10)
getInfo_btn.pack(side = LEFT, padx=(100,0))
download_btn.pack(side = RIGHT, padx=(0,100))  

fifth_frame.pack(pady = 5)

title_label.pack()
views_label.pack()
channel_label.pack()
thumbnail_lbl.pack()

bottom_frame.pack(expand = True)

# ------ Run ------ #
window.mainloop()
