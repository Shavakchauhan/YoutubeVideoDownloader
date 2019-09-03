from tkinter import *
import os
import youtube_dl
from tkinter import filedialog
root=Tk()
root.title('You Tube Downloader')
root.configure(background='snow')
root.iconbitmap('YouTube.ico')
root.geometry('1280x720')

def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        # cv2.destroyAllWindows()
root.protocol("WM_DELETE_WINDOW", on_closing)

def clear():
    et1.delete(first=0,last=80)

def browse_path():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def information():
    from tkinter import messagebox
    messagebox.showinfo(title='Success',message='Your video Downloaded')

def download():
    try:
        URL=et1.get()
        PATH=et2.get()
        ydl_opts={}
        os.chdir(PATH)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            root.title('Downloading...' + URL)
            ydl.download([URL])
        print(ydl_opts)
        noty='Your video downloaded'
        root.title(noty)
        information()
    except Exception as e:
        print(e)


folder_path = StringVar()
from PIL import Image,ImageTk

img=ImageTk.PhotoImage(Image.open('casey-horner-1400756-unsplash.jpg'))
panel=Label(root,image=img)
panel.pack(side="bottom",fill="both",expand="yes")

tag = Label(root,text = ' YouTube Video Downloader',bg = 'black',fg = 'white',width = '30',height = '1',font = ('algerian',30,'bold'))
tag.place(x = 300,y = 10)

url=Label(root,text='Enter url link',width=15,fg='red',bg='pink',height=2,font=('aerial',15,'italic'))
url.place(x=100,y=125)

path=Label(root,text='Enter path',width=15,fg='red',bg='pink',height=2,font=('aerial',15,'italic'))
path.place(x=100,y=325)



et1=Entry(root,width='30',fg='black',bg='white',font=('aerial',25,'bold'))
et1.place(x=300,y=125)

et2=Entry(root,state='disabled',textvariable=folder_path,width='30',fg='white',bg='white',font=('aerial',25,'bold'))
et2.place(x=300,y=325)

btn1 = Button(root,text = 'Clear',command = clear,width =18,fg = 'black',bg = 'lime green',activebackground = 'yellow',font=('times', 25, 'bold ') )
btn1.place(x = 900,y = 125)

btn2 = Button(root,text = 'Select path',command = browse_path,width =18,fg = 'black',bg = 'lime green',activebackground = 'azure',font=('times', 25, 'bold ') )
btn2.place(x = 900,y = 325)

download_button = Button(root,text = 'Download', command= download, width =30,fg = 'black',bg = 'lime green',activebackground = 'azure',font=('times', 25, 'bold ') )
download_button.place(x = 250,y = 525)

develop = Label(root,text = 'Developed by Shavak Chauhan',justify = 'center',width = '70',height = '1',bg = 'black',fg = 'white',font = ('times',25,'bold'))
develop.place(x = 0,y = 650)

root.mainloop()
