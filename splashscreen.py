from tkinter.ttk import Progressbar
# from tkinter import *
# from tkinter import font as f
# from tkinter import ttk
import time
from CRS import *

class Splashscreen(Frame):
    def __init__(self, master):
        super(Splashscreen, self).__init__(master)
        # self.place()
        # self.pack()
        self.grid()
        self.slide = 0
        self.font1 = f.Font(family='Yu Gothic UI Light', size=20)
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='bold')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=10)
        self.greencolor = '#48BF91'
        self.greycolor = '#252D3B'
        self.lightgreycolor = '#51545e'
        self.lightergreycolor = '#DCDCDC'
        self.whitecolor = 'white'
        self.s=ttk.Style()
        self.create_widgets()



    def create_widgets(self):
        self.f1=Frame(self,bg=self.greencolor,width=600,height=330)
        self.f1.grid(row=0,column=0)
        self.s.theme_use('clam')
        self.s.configure("red.Horizontal.TProgressbar", foreground=self.greencolor, background=self.greycolor,relief='flat')
        self.progress = Progressbar(self, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=600,mode='determinate')
        self.progress.grid(row=1,column=0)
        Label(self.f1, text='', bg=self.greencolor).grid(row=0, column=0,columnspan=2,padx=297,pady=25)
        Label(self.f1,text='C R I M E  R E P O R T I N G',bg=self.greencolor,fg=self.whitecolor,font=self.font1).grid(row=1,column=0,padx=10,sticky=W)
        Label(self.f1, text='S Y S T E M', bg=self.greencolor, fg=self.whitecolor, font=self.font1).grid(row=2, column=0, padx=10, sticky=W)
        Label(self.f1, text='P o w e r e d  b y  N H S  G r o u p  3', bg=self.greencolor, fg=self.whitecolor, font=self.font4).grid(row=3, column=0, padx=10,pady=5, sticky=W)
        Label(self.f1, text='', bg=self.greencolor,fg=self.whitecolor).grid(row=4, column=0, columnspan=2, pady=30)
        #Button(self.f1,text='G E T  S T A R T E D',height=2,bg=self.whitecolor,fg=self.greencolor,border=0,command=self.bar).grid(row=4,column=0, columnspan=2,pady=20)
        self.load=Label(self.f1, text='', bg=self.greencolor,font=self.font4, fg=self.whitecolor)
        self.load.grid(row=5, column=0, columnspan=2, pady=20)
        self.after(2000, self.bar)

    def bar(self):
        self.load.config(text='I n i t i a l i z i n g . . .')
        self.timer=0
        for i in range(110):
            self.progress['value']=self.timer
            self.update_idletasks()
            time.sleep(0.03)
            self.timer+=1
        self.master.destroy()
        login()


if __name__=="__main__":
    root = Tk()
    root.resizable(0, 0)
    app_width=600
    app_height=350
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x= (screen_width/2) - (app_width/2)
    y= (screen_height/2) - (app_height/2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    root.overrideredirect(1)
    app = Splashscreen(root)
    app.mainloop()