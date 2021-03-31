# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:38:17 2021

@author: skama
"""
!pip install pytube

##Importing libraries
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog


##Creating  base object
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 10 ').pack()

## Creating URL link space
link = StringVar()
Label(root, text = 'Paste URL link Here:', font = 'arial 10 bold').place(x= 150 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
##Selecting resolution qulity
quality_option=Label(root,text="Please select the quality that you want to choose for your video",font='arial 8').place(x=100,y=120)
option=['240p','360p','480p','720p']
quality=ttk.Combobox(root,values=option)
quality.place(x=200,y=150)
##File path saved 
directory=StringVar()
def save_file():
    saveFilePath  =  filedialog.asksaveasfilename(title = "Select file",filetypes =[("MPEG-4 Video","*.mp4")])
    directory.set(saveFilePath)
   
    
#Creating a link for download
#link2=StringVar()
#Label(root,text='Please specify the destination folder',font='arial 8').place(x=100,y=180)
#link2_enter=Entry(root,width=50,textvariable=link2).place(x=100,y=210)

#Creating a button for saving file
btn=ttk.Button(root,text='Save File',command=lambda:save_file())
btn.place(x=190,y=210)


##Download function
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.filter(res=str(quality.get())).first()
    video.download(str( directory.get()))
    Label(root, text = "Your video has been downloaded", font = 'arial 15').place(x= 200 , y = 240)  
Button(root,text = 'DOWNLOAD VIDEO', font = 'arial 15 ' ,bg = 'red', padx = 2, command = Downloader).place(x=190 ,y = 250)
root.mainloop()
