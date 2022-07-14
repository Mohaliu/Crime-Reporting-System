from tkinter import *
from tkinter import font as f
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import *
from tkinter import filedialog
from time import strftime
import numpy as np
import string
import mplcursors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# from userdashboard import *
import sqlite3

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master=master
        # self.place()
        # self.pack()
        self.grid()
        self.slide=0
        self.font1=f.Font(family='Yu Gothic UI Light', size=15)
        self.font2 = f.Font(family='Yu Gothic UI Light', size=10, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=10)
        self.greencolor = '#48BF91'
        self.greycolor = '#252D3B'
        self.lightgreycolor = '#51545e'
        self.lightergreycolor = '#DCDCDC'
        self.whitecolor='white'
        self.database()
        self.create_widgets()

    def create_widgets(self):
        #LEFT FRAME DESIGN SEGMENT
        self.frame1=Frame(self.master,width=350,height=500,bg=self.greencolor)
        self.frame1.grid(row=0,column=0, sticky='nsew')
        self.img5 = ImageTk.PhotoImage(Image.open("cancel.png"))
        Button(self.frame1,image=self.img5, command=self.master.destroy,cursor='hand2',bg=self.greencolor,borderwidth=0).grid(row=0,column=0,sticky=W)
        self.img4 = ImageTk.PhotoImage(Image.open("three.png"))
        Label(self.frame1,image=self.img4, bg=self.greencolor).grid(row=1,column=0,columnspan=2,pady=5)
        self.lbl_hello=Label(self.frame1,text='H E L L O !', fg= self.whitecolor,bg=self.greencolor,font=self.font1)
        self.lbl_hello.grid(row=2,column=0)
        Label(self.frame1,text='',bg=self.greencolor).grid(row=3,column=0,columnspan=2)
        self.lbl_stuff = Label(self.frame1, text='Check and update your details\nOn your dashboard', fg= self.whitecolor, bg=self.greencolor,font=self.font1)
        self.lbl_stuff.grid(row=4,column=0)
        self.img = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.img1 = ImageTk.PhotoImage(Image.open("crime-file.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("time.png"))
        self.img3 = ImageTk.PhotoImage(Image.open("inspection.png"))
        self.photo=Label(self.frame1, image=self.img, border=0, bg=self.greencolor, fg= self.whitecolor)
        self.photo.grid(row=5,column=0,padx=111,pady=10)
        Label(self.frame1,text='Powered by NHS group 3', font=self.font2,bg=self.greencolor, fg= self.whitecolor).grid(row=6,column=0,pady=80, columnspan=2,sticky='s')
        self.slideshow()

        #RIGHT FRAME DESIGN SEGMENT
        self.frame2 = Frame(self.master, width=350, height=500, bg=self.greycolor)
        self.frame2.grid(row=0, column=1, sticky='nsew')

        #dividing into two sub frames
        self.frame2a=Frame(self.frame2,width=350,height=100, bg=self.greycolor)
        self.frame2a.grid(row=0,column=0, columnspan=2)

        # frame2a design segment
        Label(self.frame2a,text='',bg=self.greycolor).grid(row=0,column=0,columnspan=3,padx=100,pady=10)
        self.sign_in_btn=Button(self.frame2a,text='Sign In',fg= self.lightergreycolor,cursor='hand2',bg= self.lightgreycolor,font=self.font4,border=0, command=self.sign_in)
        self.sign_in_btn.grid(row=0,column=3,sticky=E)
        self.sign_up_btn = Button(self.frame2a, text='Sign Up',cursor='hand2', bg=self.greencolor,fg= self.whitecolor,border=0,font=self.font3, command=self.sign_up)
        self.sign_up_btn.grid(row=0, column=4,sticky=W)
        Label(self.frame2a, text='', bg=self.greycolor).grid(row=1, column=0,pady=1)
        self.sign_in_lbl=Label(self.frame2a,text='Sign In',cursor='hand2',fg= self.whitecolor,bg=self.greycolor,font=self.font1)
        self.sign_in_lbl.grid(row=2,column=0)
        self.sign_in_lbl.bind("<Button-1>", self.sign_in_label)
        Label(self.frame2a,text='or',width=2,fg= self.lightgreycolor,bg=self.greycolor,font=self.font3).grid(row=2,column=1)
        self.sign_up_lbl=Label(self.frame2a,text='Sign Up',cursor='hand2',fg= self.lightgreycolor,bg=self.greycolor,font=self.font3)
        self.sign_up_lbl.grid(row=2,column=2)
        self.sign_up_lbl.bind('<Button-1>', self.sign_up_label)
        Label(self.frame2a, text='', bg=self.greycolor).grid(row=2, column=3,columnspan=2, padx=61)
        self.sep = Frame(self.frame2a,width=70,height=2,bg=self.greencolor)
        self.sep.grid(row=3,column=0)
        self.sep1 = Frame(self.frame2a, width=70, height=2, bg=self.greycolor)
        self.sep1.grid(row=3, column=2)

        # frame2b design segment(it is divided into 2[sign up or sign in])
        #SIGN IN SEGMENT
        self.frame2bi = Frame(self.frame2, width=350, height=400, bg=self.greycolor)
        self.frame2bi.grid(row=1, column=0, columnspan=2)
        Label(self.frame2bi, text='', bg=self.greycolor).grid(row=0, column=0, padx=100,pady=15)
        self.lbl_email=Label(self.frame2bi,text='E-MAIL', bg=self.greycolor,fg=self.whitecolor,font=self.font2)
        self.lbl_email.grid(row=1,column=0,sticky=W,padx= 32)
        self.ent_email=Entry(self.frame2bi,width='45', bg=self.greycolor,border=0,fg=self.whitecolor,font=self.font4)
        self.ent_email.grid(row=2,column=0,sticky=W,padx= 35,columnspan=2)
        Frame(self.frame2bi, width=275, height=1, bg=self.lightgreycolor).grid(row=3, column=0,sticky=W,padx=35)
        Label(self.frame2bi, text='', bg=self.greycolor).grid(row=4, column=0, padx=180,pady=15)
        self.lbl_pass=Label(self.frame2bi,text='PASSWORD', bg=self.greycolor,fg=self.whitecolor,font=self.font2)
        self.lbl_pass.grid(row=5,column=0,sticky=W,padx= 32)
        self.ent_pass=Entry(self.frame2bi,width='45',show='*', bg=self.greycolor,border=0,fg=self.whitecolor,font=self.font4)
        self.ent_pass.grid(row=6,column=0,sticky=W,padx = 35,columnspan=2)
        Frame(self.frame2bi, width=275, height=1, bg=self.lightgreycolor).grid(row=7, column=0,sticky=W,padx=35)
        Label(self.frame2bi, text='', bg=self.greycolor).grid(row=8, column=0, padx=180, pady=15)
        self.loginbtn = Button(self.frame2bi, text='Sign In',cursor='hand2',width=9, bg=self.greencolor, fg=self.whitecolor, border=0,font=self.font3, command=self.signinmain)
        self.loginbtn.grid(row=9, column=0,sticky=W,padx= 33)
        self.anon = Button(self.frame2bi, text='Anonymous crime report',cursor='hand2', bg=self.lightgreycolor, fg=self.whitecolor, border=0,font=self.font3, command=self.anonymous)
        self.anon.grid(row=10, column=0,sticky=W,padx= 33, pady=10)
        self.loginbtn.bind("<Enter>", self.on_enter)
        self.loginbtn.bind("<Leave>", self.on_leave)


        # SIGN UP SEGMENT
        self.frame2bii = Frame(self.frame2, width=350, height=400, bg=self.greycolor)
        Label(self.frame2bii, text='', bg=self.greycolor).grid(row=0, column=0, padx=100, pady=2)
        self.lbl_fullname = Label(self.frame2bii, text='FULL NAME', bg=self.greycolor, fg=self.whitecolor, font=self.font2)
        self.lbl_fullname.grid(row=1, column=0, sticky=W, padx=32)
        self.ent_fullname = Entry(self.frame2bii, width='45', bg=self.greycolor, border=0, fg=self.whitecolor,font=self.font4)
        self.ent_fullname.grid(row=2, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.frame2bii, width=275, height=1, bg=self.lightgreycolor).grid(row=3, column=0, sticky=W, padx=35)
        Label(self.frame2bii, text='', bg=self.greycolor).grid(row=4, column=0, padx=180)
        self.lbl_mail = Label(self.frame2bii, text='E-MAIL', bg=self.greycolor, fg=self.whitecolor, font=self.font2)
        self.lbl_mail.grid(row=5, column=0, sticky=W, padx=32)
        self.ent_mail = Entry(self.frame2bii, width='45', bg=self.greycolor, border=0, fg=self.whitecolor,font=self.font4)
        self.ent_mail.grid(row=6, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.frame2bii, width=275, height=1, bg=self.lightgreycolor).grid(row=7, column=0, sticky=W, padx=35)
        Label(self.frame2bii, text='', bg=self.greycolor).grid(row=8, column=0, padx=180)
        self.lbl_number = Label(self.frame2bii, text='PHONE NUMBER', bg=self.greycolor, fg=self.whitecolor, font=self.font2)
        self.lbl_number.grid(row=9, column=0, sticky=W, padx=32)
        self.ent_number = Entry(self.frame2bii, width='45', bg=self.greycolor, border=0, fg=self.whitecolor,font=self.font4)
        self.ent_number.grid(row=10, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.frame2bii, width=275, height=1, bg=self.lightgreycolor).grid(row=11, column=0, sticky=W, padx=35)
        Label(self.frame2bii, text='', bg=self.greycolor).grid(row=12, column=0, padx=180)
        self.lbl_password = Label(self.frame2bii, text='PASSWORD', bg=self.greycolor, fg=self.whitecolor, font=self.font2)
        self.lbl_password.grid(row=13, column=0, sticky=W, padx=32)
        self.ent_password = Entry(self.frame2bii, width='45',show='*', bg=self.greycolor, border=0, fg=self.whitecolor,font=self.font4)
        self.ent_password.grid(row=14, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.frame2bii, width=275, height=1, bg=self.lightgreycolor).grid(row=15, column=0, sticky=W, padx=35)
        Label(self.frame2bii, text='', bg=self.greycolor).grid(row=16, column=0, padx=180)
        #Label(self.frame2bii, text='', bg=self.greycolor).grid(row=8, column=0, padx=180, pady=15)
        self.signup = Button(self.frame2bii, text='Sign Up',cursor='hand2', width=9, bg=self.greencolor, fg=self.whitecolor, border=0,font=self.font3, command=self.signupmain)
        self.signup.grid(row=17, column=0, sticky=W, padx=33,pady=15)
        self.signup.bind("<Enter>", self.on_enter)
        self.signup.bind("<Leave>", self.on_leave)

    def on_enter(self,e):
        self.signup.config(background=self.lightgreycolor,foreground=self.lightergreycolor)
        self.loginbtn.config(background=self.lightgreycolor,foreground=self.lightergreycolor)

    def on_leave(self,e):
        self.signup.config(background=self.greencolor,foreground=self.whitecolor)
        self.loginbtn.config(background=self.greencolor,foreground=self.whitecolor)




    #for the left frame slideshow
    def slideshow(self):
        if self.slide==5:
            self.slide=1
        if self.slide==1:
            self.lbl_stuff.config(text='If you see something say something\nReport any crimes witnessed')
            self.photo.config(image=self.img1)
        elif self.slide == 2:
            self.lbl_stuff.config(text='You have the rights to view\nprevious reports')
            self.photo.config(image=self.img2)
        elif self.slide==3:
            self.lbl_stuff.config(text='Any crimes reported will be investigated\nKeep checking for updates')
            self.photo.config(image=self.img3)
        elif self.slide==4:
            self.lbl_stuff.config(text='Check and update your details\nOn your dashboard')
            self.photo.config(image=self.img)
        self.slide+=1
        self.after(2000, self.slideshow)

    def sign_in_label(self,e):
        self.sep.config(bg=self.greencolor)
        self.sign_in_lbl.config(fg= self.whitecolor,font=self.font1)
        self.sep1.config(bg=self.greycolor)
        self.sign_up_lbl.config(fg= self.lightgreycolor,font=self.font3)
        self.sign_up_btn.config(bg=self.greencolor,fg=self.whitecolor, font=self.font3)
        self.sign_in_btn.config(fg=self.lightergreycolor,bg=self.lightgreycolor,font=self.font4)
        self.frame2bii.grid_forget()
        self.frame2bi.grid(row=1, column=0, columnspan=2)

    def sign_up_label(self,e):
        self.sep1.config(bg=self.greencolor)
        self.sign_up_lbl.config(fg= self.whitecolor,font=self.font1)
        self.sep.config(bg=self.greycolor)
        self.sign_in_lbl.config(fg= self.lightgreycolor,font=self.font3)
        self.sign_in_btn.config(bg=self.greencolor, fg=self.whitecolor, font=self.font3)
        self.sign_up_btn.config(fg=self.lightergreycolor, bg=self.lightgreycolor, font=self.font4)
        self.frame2bi.grid_forget()
        self.frame2bii.grid(row=1, column=0, columnspan=2)

    def sign_in(self):
        self.sep.config(bg=self.greencolor)
        self.sign_in_lbl.config(fg= self.whitecolor,font=self.font1)
        self.sep1.config(bg=self.greycolor)
        self.sign_up_lbl.config(fg= self.lightgreycolor,font=self.font3)
        self.sign_up_btn.config(bg=self.greencolor,fg=self.whitecolor, font=self.font3)
        self.sign_in_btn.config(fg=self.lightergreycolor,bg=self.lightgreycolor,font=self.font4)
        self.frame2bii.grid_forget()
        self.frame2bi.grid(row=1, column=0, columnspan=2)

    def sign_up(self):
        self.sep1.config(bg=self.greencolor)
        self.sign_up_lbl.config(fg= self.whitecolor,font=self.font1)
        self.sep.config(bg=self.greycolor)
        self.sign_in_lbl.config(fg= self.lightgreycolor,font=self.font3)
        self.sign_in_btn.config(bg=self.greencolor, fg=self.whitecolor, font=self.font3)
        self.sign_up_btn.config(fg=self.lightergreycolor, bg=self.lightgreycolor, font=self.font4)
        self.frame2bi.grid_forget()
        self.frame2bii.grid(row=1, column=0, columnspan=2)

    def signupmain(self):
        if self.ent_fullname.get()=='' or self.ent_mail.get()=='' or self.ent_number.get()=='' or self.ent_password.get()=='':
            messagebox.showerror('ERROR', 'All fields are required')
            print('some fields not filled')
        else:
            conn=sqlite3.connect("user_data2.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM user_details WHERE email=?",[(self.ent_mail.get())])
            email = cursor.fetchall()
            if email or self.ent_mail.get().lower()=='admin':
                messagebox.showerror("ERROR","User already exists\nTry another Email")

            else:
                stmt="INSERT INTO user_details(name,email,phone,password) VALUES(?, ?, ?, ?)"
                entries=[(self.ent_fullname.get().lower(), self.ent_mail.get().lower(), self.ent_number.get().lower(), self.ent_password.get())]
                cursor.executemany(stmt,entries)
                conn.commit()
                conn.close()
                messagebox.showinfo('Welcome!','Account created successfully\nProceeding to login... ')
                self.ent_fullname.delete(0, END)
                self.ent_mail.delete(0, END)
                self.ent_number.delete(0, END)
                self.ent_password.delete(0, END)
                self.sign_in()

    def signinmain(self):
        if self.ent_email.get() == '' or self.ent_pass.get() == '':
            messagebox.showerror('ERROR', 'All fields are required')
            print('some fields not filled')
        elif self.ent_email.get() == 'admin' and self.ent_pass.get() == '123':
            messagebox.showinfo('welcome','hello admin')
            self.master.withdraw()
            self.ent_email.delete(0, END)
            self.ent_pass.delete(0, END)
            self.adminWindow=Toplevel(self.master)
            self.adminWindow.resizable(0, 0)
            self.adminWindow.configure(bg='#303A48')
            self.adminWindow.geometry('1200x690+83+10')
            self.adminWindow.overrideredirect(1)
            apk = Admindashboard(self.adminWindow)
        else:
            conn = sqlite3.connect("user_data2.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM user_details WHERE email=? AND password=?", [(self.ent_email.get().lower()),(self.ent_pass.get())])
            results=cursor.fetchall()
            if results:
                user=[]
                messagebox.showinfo('WELCOME USER','Logged in successfully')
                for i in results[0]:
                    user.append(i)
                conn.close()
                self.master.withdraw()
                self.ent_email.delete(0, END)
                self.ent_pass.delete(0, END)
                self.userWindow = Toplevel(self.master)
                self.userWindow.resizable(0, 0)
                self.userWindow.overrideredirect(1)
                self.userWindow.geometry('1200x690+83+4')
                apk = Userdashboard(self.userWindow, user)

            else:
                messagebox.showerror('ERROR','Invalid username or password')
                print('invalid username or password')


    def database(self):
        with sqlite3.connect('user_data2.db') as conn:
            cursor=conn.cursor()
            stmt="CREATE TABLE IF NOT EXISTS user_details(email varchar(40) primary key, name varchar(40), phone varchar(15), password varchar(15),picture BLOB)"
            cursor.execute(stmt)
            stmt2="CREATE TABLE IF NOT EXISTS crime_data(date varchar(10),state varchar(15),address varchar(80), crime varchar(30),description varchar(200),email varchar(40),evidence BLOB, FOREIGN KEY(email) REFERENCES user_details(email))"
            cursor.execute(stmt2)
            conn.commit()

    def anonymous(self):
        self.master.withdraw()
        self.anonWindow = Toplevel(self.master)
        self.anonWindow.resizable(0, 0)
        # self.anonWindow.configure(bg=self.greycolor)
        self.anonWindow.overrideredirect(1)
        app_width = 700
        app_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.anonWindow.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        apk = Anonymousreport(self.anonWindow)



class Anonymousreport(Frame):
    def __init__(self, main):
        super(Anonymousreport, self).__init__(main)
        self.main=main
        self.font1=f.Font(family='Yu Gothic UI Light', size=20)
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=10)
        self.greencolor = '#48BF91'
        self.greycolor = '#252D3B'
        self.lightgreycolor = '#51545e'
        self.lightergreycolor = '#DCDCDC'
        self.whitecolor='white'
        self.states = [
            'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta',
            'Ebonyi', 'Edo',
            'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos',
            'Nasarawa', 'Niger',
            'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara', 'FCT(ABUJA)'
        ]
        self.crimes = [
            'Aggravated Assault', 'Aiding and Abetting',  'Arson',
            'Assault / Battery', 'Attempted murder', 'Bribery', 'Burglary', 'Child Abuse',
            'Child Pornography', 'Computer Crime', 'Conspiracy', 'Credit / Debit Card Fraud','Criminal Contempt of Court',
            'Cyberbullying','Domestic Violence', 'Disorderly Conduct','Disturbing the Peace', 'Drug Possession',
            'Drug Trafficking', 'Drug Manufacturing','Extortion','Forgery', 'Fraud', 'Harassment',
            'Homicide', 'Identity Theft', 'Indecent Exposure','Insurance Fraud','Kidnapping','Manslaughter','Money Laundering', 'Murder',
            'Perjury','Probation Violation','Prostitution',  'Public Intoxication', 'Pyramid Schemes', 'Rape', 'Robbery',
            'Racketeering / RICO','Securities Fraud','Sexual Assault',  'Shoplifting', 'Solicitation', 'Stalking',
            'Statutory Rape', 'Theft', 'Vandalism', 'Wire Fraud'
        ]
        self.create_widgets()

    def create_widgets(self):
        self.reportframe = Frame(self.main, bg=self.greycolor, width=900, height=470)
        self.reportframe.grid(row=1, column=1,sticky='nsew')
        Label(self.reportframe, text='R E P O R T  C R I M E  A N O N Y M O U S L Y', bg=self.greycolor, font=self.font1,
              fg=self.whitecolor).grid(row=0, column=0, columnspan=3, padx=32, pady=(25, 10), sticky=NW)
        Label(self.reportframe, text='D A T E  O F  C R I M E :', bg=self.greycolor, font=self.font2,
              fg=self.whitecolor).grid(row=1, column=0, padx=(32, 3), pady=10, sticky=NW)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox', fieldbackground=self.greencolor, background=self.greencolor,
                        foreground=self.whitecolor)
        style.map('TCombobox', fieldbackground=[('readonly', self.greencolor)])
        style.map('TCombobox', selectbackground=[('readonly', self.greencolor)])
        self.cal = DateEntry(self.reportframe, selectmode='day', font=self.font2, year=2022)
        self.cal['state'] = 'readonly'
        self.cal.grid(row=1, column=1, sticky=NW, pady=10)
        self.lbl_location = Label(self.reportframe, text='L O C A T I O N  O F  C R I M E :', bg=self.greycolor,font=self.font2, fg=self.whitecolor)
        self.lbl_location.grid(row=2, column=0, columnspan=3, padx=32, pady=10, sticky=NW)
        Label(self.reportframe, text='S T A T E :', bg=self.greycolor, font=self.font2, fg=self.whitecolor).grid(row=3,column=0,padx=(32, 3),pady=10,sticky=W)
        self.combo_state = ttk.Combobox(self.reportframe, value=self.states, font=self.font2, width=12)
        self.combo_state['state'] = 'readonly'
        self.combo_state.set('STATES')
        self.combo_state.grid(row=3, column=1, pady=10, sticky=NW)
        Label(self.reportframe, text='A D D R E S S :', bg=self.greycolor, font=self.font2, fg=self.whitecolor).grid(
            row=4, column=0, padx=(32, 3), pady=10, sticky=NW)
        # self.combo_state.bind("<<ComboboxSelected>>", comboclick)
        self.ent_address = Entry(self.reportframe, width=50, bg=self.greencolor, border=0, fg=self.whitecolor,
                                 font=self.font3)
        self.ent_address.grid(row=4, column=1, sticky=NW, pady=10)
        Label(self.reportframe, text='T Y P E  O F  C R I M E :', bg=self.greycolor, font=self.font2,
              fg=self.whitecolor).grid(
            row=5, column=0, padx=(32, 3), pady=10, sticky=NW)
        self.combo_crime = ttk.Combobox(self.reportframe, value=self.crimes, font=self.font2, width=25)
        self.combo_crime['state'] = 'readonly'
        self.combo_crime.set('CRIMES')
        self.combo_crime.grid(row=5, column=1, pady=10, sticky=NW)
        Label(self.reportframe, text='D E S C R I P T I O N :', bg=self.greycolor, font=self.font2,
              fg=self.whitecolor).grid(
            row=6, column=0, padx=(32, 3), pady=10, sticky=NW)
        self.ent_desc = Entry(self.reportframe, width=50, bg=self.greencolor, border=0, fg=self.whitecolor,
                              font=self.font3)
        self.ent_desc.grid(row=6, column=1, sticky=NW, pady=10, columnspan=3)
        self.uploadevdc = Button(self.reportframe, text='UPLOAD EVIDENCE', cursor='hand2', bg=self.lightgreycolor,
                                 fg=self.whitecolor, border=0, font=self.font3, command=self.uploadevidence)
        self.uploadevdc.grid(row=7, column=0, sticky=W, padx=33, pady=(10, 0))
        self.quitanon = Button(self.reportframe, text='Cancel', cursor='hand2', width=9, bg='#A5494F',
                           fg=self.whitecolor, border=0, font=self.font3, command=self.Quitanon)
        self.quitanon.grid(row=8, column=0, sticky=W,padx=33, pady=(20, 80))
        self.rprt = Button(self.reportframe, text='Report', cursor='hand2', width=9, bg=self.greencolor,
                           fg=self.whitecolor, border=0, font=self.font3, command=self.submitreport)
        self.rprt.grid(row=8, column=1, sticky=W,padx=(365,30), pady=(20, 80))


    def submitreport(self):
        if self.combo_state.get() == 'STATES' or self.cal.get() == '' or self.combo_crime.get() == 'CRIMES' or self.ent_address.get() == '' or self.ent_desc.get() == '':
            messagebox.showerror('ERROR', 'All fields are required')
            # print('some fields not filled')
        else:
            try:
                conn = sqlite3.connect("user_data2.db")
                cursor = conn.cursor()
                stmt = "INSERT INTO crime_data(date,state,address,crime,description,email,evidence,status) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                entries = [(self.cal.get(), self.combo_state.get(), self.ent_address.get(), self.combo_crime.get(),
                            self.ent_desc.get(), "Anonymous", self.evdnc, "PENDING")]
                cursor.executemany(stmt, entries)
                conn.commit()
                conn.close()
                self.uploadevdc.config(bg=self.lightgreycolor)
                self.ent_address.delete(0, END)
                self.ent_desc.delete(0, END)
                self.combo_state.set('STATES')
                self.combo_crime.set('CRIMES')
                messagebox.showinfo('success!', 'report successful ')

            except:
                messagebox.showerror('error', 'no evidence uploaded')

    def uploadevidence(self):
        try:
            self.getevidence = filedialog.askopenfilename(title="SELECT IMAGE", filetypes=(
            ("jpg", "*jpg"), ("jpeg", "*jpeg"), ("png", "*.png"), ("Allfile", "*.*")))
            if self.getevidence:
                self.uploadevdc.config(bg=self.greencolor)
                with open(self.getevidence, 'rb') as f:
                    self.evdnc = f.read()
            else:
                messagebox.showerror('ERROR', 'No image selected')
        except:
            messagebox.showerror('ERROR', 'No image selected')

    def Quitanon(self):
        self.master.destroy()
        self.master.master.deiconify()



class Userdashboard(Frame):
    def __init__(self, master,profile):
    # def __init__(self, master):
        super(Userdashboard, self).__init__(master)
        self.master=master
        # self.place()
        # self.pack()
        self.grid()
        self.slide=0
        self.font1=f.Font(family='Yu Gothic UI Light', size=20)
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=13)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=10)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='bold')
        self.greencolor = '#48BF91'
        self.greycolor = '#252D3B'
        self.lightgreycolor = '#51545e'
        self.lightergreycolor = '#DCDCDC'
        self.whitecolor='white'
        self.darkgreycolor='#363942'
        self.email=profile[0]
        self.name=profile[1]
        self.phonemum=profile[2]
        # self.email='egbudomraphael@gmail.com'
        # self.name='egbudom raphael'
        # self.phonemum='08091516236'
        self.states = [
            'Abia', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta',
            'Ebonyi', 'Edo',
            'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos',
            'Nasarawa', 'Niger',
            'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara', 'FCT(ABUJA)'
        ]
        self.crimes = [
            'Aggravated Assault', 'Aiding and Abetting',  'Arson',
            'Assault / Battery', 'Attempted murder', 'Bribery', 'Burglary', 'Child Abuse',
            'Child Pornography', 'Computer Crime', 'Conspiracy', 'Credit / Debit Card Fraud','Criminal Contempt of Court',
            'Cyberbullying','Domestic Violence', 'Disorderly Conduct','Disturbing the Peace', 'Drug Possession',
            'Drug Trafficking', 'Drug Manufacturing','Extortion','Forgery', 'Fraud', 'Harassment',
            'Homicide', 'Identity Theft', 'Indecent Exposure','Insurance Fraud','Kidnapping','Manslaughter','Money Laundering', 'Murder',
            'Perjury','Probation Violation','Prostitution',  'Public Intoxication', 'Pyramid Schemes', 'Rape', 'Robbery',
            'Racketeering / RICO','Securities Fraud','Sexual Assault',  'Shoplifting', 'Solicitation', 'Stalking',
            'Statutory Rape', 'Theft', 'Vandalism', 'Wire Fraud'
        ]
        self.slideshow()
        self.display()
        self.create_widgets()


    def create_widgets(self):
        #User dashboard is divided into 3 frames
        self.frame1=Frame(self.master,bg=self.greycolor,width=300,height=690)
        self.frame1.grid(row=0,column=0,rowspan=2,sticky='nsew')
        self.img=ImageTk.PhotoImage(Image.open("police-badge.png"))
        self.img1=ImageTk.PhotoImage(Image.open("justice-scale.png"))
        self.img2=ImageTk.PhotoImage(Image.open("spy.png"))
        self.img3=ImageTk.PhotoImage(Image.open("crime-investigation.png"))
        self.pfp=Label(self.frame1,image=self.img,bg=self.greycolor)
        self.pfp.grid(row=0,column=0,sticky=S,pady=40)
        self.lbl_name=Label(self.frame1,font=self.font2,text=f'W E L C O M E\n{self.name.upper()}',bg=self.greycolor,fg=self.greencolor)
        self.lbl_name.grid(row=1,column=0,sticky=N)
        Frame(self.frame1,width=250,height=1,bg=self.greencolor).grid(row=2,column=0,pady=10)
        Label(self.frame1,text='',bg=self.greycolor).grid(row=3,column=0,pady=10)
        self.dash=Button(self.frame1,width=37,pady=4,text='D A S H B O A R D',font=self.font2,cursor='hand2',border=0,bg=self.greencolor,fg=self.whitecolor,command=lambda: self.cmd1(0))
        self.dash.grid(row=4,column=0,sticky=N)
        self.report = Button(self.frame1,width=37,pady=4, text='R E P O R T  C R I M E',font=self.font2,cursor='hand2',border=0,bg=self.greycolor,fg=self.greencolor,command=lambda: self.cmd1(1))
        self.report.grid(row=5,column=0,sticky=N)
        self.history = Button(self.frame1,width=37,pady=4, text='R E P O R T  H I S T O R Y', font=self.font2,cursor='hand2',border=0,bg=self.greycolor,fg=self.greencolor,command=lambda: self.cmd1(2))
        self.history.grid(row=6,column=0,sticky=N)
        self.check = Button(self.frame1,width=37,pady=4, text='C H E C K  R E P O R T  S T A T U S', font=self.font2,cursor='hand2',border=0,bg=self.greycolor,fg=self.greencolor,command=lambda: self.cmd1(3))
        self.check.grid(row=7,column=0,sticky=N)
        self.edit=Button(self.frame1,width=37,pady=4,text='E D I T  P R O F I L E',font=self.font2,border=0,cursor='hand2',bg=self.greycolor,fg=self.greencolor,command=lambda: self.cmd1(4))
        self.edit.grid(row=8,column=0,sticky=N)
        Frame(self.frame1,width=1,height=600,bg=self.greencolor).place(x=301,y=45)
        Label(self.frame1,text='',bg=self.greycolor).grid(row=8,column=0,pady=51)
        self.logout=Button(self.frame1,width=16,height=2,text='L O G O U T',font=self.font2,border=0,cursor='hand2',bg=self.greencolor,fg=self.greycolor,command=self.logout)
        self.logout.grid(row=9,column=0)
        self.logout.bind('<Enter>', lambda e: self.on_enter(e, 0))
        self.logout.bind('<Leave>', lambda e: self.on_leave(e, 0))

        #frame 2 design
        self.frame2 = Frame(self.master,bg=self.greycolor, width=900, height=140)
        self.frame2.grid(row=0, column=1, sticky='nsew')
        self.img4 = ImageTk.PhotoImage(Image.open("delete.png"))
        self.closebtn=Button(self.frame2, image=self.img4, command=self.master.master.destroy,cursor='hand2', bg=self.greycolor, borderwidth=0)
        self.closebtn.grid(row=0, column=5,sticky=W)
        Label(self.frame2,text='',bg=self.greycolor).grid(row=1,column=0,pady=30)

        self.dashbtn=Button(self.frame2,text='D A S H\nB O A R D',font=self.font4,cursor='hand2',width=15, height=6,border=0,bg=self.darkgreycolor,fg=self.greencolor,command=lambda: self.cmd1(0))
        self.dashbtn.grid(row=2,column=0,padx=33)
        self.reportbtn=Button(self.frame2,text='R E P O R T\nC R I M E',font=self.font4,cursor='hand2',width=15, height=6,border=0,bg=self.greencolor,fg=self.whitecolor,command=lambda: self.cmd1(1))
        self.reportbtn.grid(row=2,column=1,padx=33)
        self.historybtn=Button(self.frame2,text='R E P O R T\nH I S T O R Y',font=self.font4,cursor='hand2',width=15, height=6,border=0,bg=self.greencolor,fg=self.whitecolor,command=lambda: self.cmd1(2))
        self.historybtn.grid(row=2,column=2,padx=33)
        self.checkbtn=Button(self.frame2,text='C H E C K\nR E P O R T\nS T A T U S',font=self.font4,cursor='hand2',width=15, height=6,border=0,bg=self.greencolor,fg=self.whitecolor,command=lambda: self.cmd1(3))
        self.checkbtn.grid(row=2,column=3,padx=32)
        self.editbtn=Button(self.frame2,text='E D I T\nP R O F I L E',font=self.font4,cursor='hand2',width=15, height=6,border=0,bg=self.greencolor,fg=self.whitecolor,command=lambda: self.cmd1(4))
        self.editbtn.grid(row=2,column=4,padx=32)
        self.f1= Frame(self.frame2,width=111,height=4,bg=self.greencolor)
        self.f1.grid(row=3,column=0)
        self.f2 = Frame(self.frame2, width=111, height=4, bg=self.greycolor)
        self.f2.grid(row=3, column=1)
        self.f3 = Frame(self.frame2, width=111, height=4, bg=self.greycolor)
        self.f3.grid(row=3, column=2)
        self.f4 = Frame(self.frame2, width=111, height=4, bg=self.greycolor)
        self.f4.grid(row=3, column=3)
        self.f5 = Frame(self.frame2, width=111, height=4, bg=self.greycolor)
        self.f5.grid(row=3, column=4)

        self.btns=[self.dashbtn,self.reportbtn,self.historybtn,self.checkbtn,self.editbtn]
        self.btns2=[self.dash,self.report,self.history,self.check,self.edit]
        self.f=[self.f1,self.f2,self.f3,self.f4,self.f5]
        self.var=[True,False,False,False,False]

        self.dashbtn.bind('<Enter>', lambda e: self.on_enter2(e, 0))
        self.dashbtn.bind('<Leave>', lambda e: self.on_leave2(e, 0))
        self.reportbtn.bind('<Enter>', lambda e: self.on_enter2(e, 1))
        self.reportbtn.bind('<Leave>', lambda e: self.on_leave2(e, 1))
        self.historybtn.bind('<Enter>', lambda e: self.on_enter2(e, 2))
        self.historybtn.bind('<Leave>', lambda e: self.on_leave2(e, 2))
        self.checkbtn.bind('<Enter>', lambda e: self.on_enter2(e, 3))
        self.checkbtn.bind('<Leave>', lambda e: self.on_leave2(e, 3))
        self.editbtn.bind('<Enter>', lambda e: self.on_enter2(e, 4))
        self.editbtn.bind('<Leave>', lambda e: self.on_leave2(e,4))

        self.dash.bind('<Enter>', lambda e: self.on_enter2(e, 0))
        self.dash.bind('<Leave>', lambda e: self.on_leave2(e, 0))
        self.report.bind('<Enter>', lambda e: self.on_enter2(e, 1))
        self.report.bind('<Leave>', lambda e: self.on_leave2(e, 1))
        self.history.bind('<Enter>', lambda e: self.on_enter2(e, 2))
        self.history.bind('<Leave>', lambda e: self.on_leave2(e, 2))
        self.check.bind('<Enter>', lambda e: self.on_enter2(e, 3))
        self.check.bind('<Leave>', lambda e: self.on_leave2(e, 3))
        self.edit.bind('<Enter>', lambda e: self.on_enter2(e, 4))
        self.edit.bind('<Leave>', lambda e: self.on_leave2(e,4))

        # Dashboard section
        self.dashframe = Frame(self.master,bg=self.greycolor, width=900, height=470)
        self.dashframe.grid(row=1, column=1,sticky='nsew')
        self.pic=ImageTk.PhotoImage(Image.open(self.profilepic))
        self.image = Image.open(self.profilepic)
        resized = self.image.resize((128, 128))
        self.pic = ImageTk.PhotoImage(resized)
        self.picture=Label(self.dashframe,image=self.pic,bg=self.darkgreycolor)
        self.picture.grid(row=0,column=0,padx=34,pady=60,rowspan=2,sticky='nw')
        Label(self.dashframe,text='FULL NAME:',font=self.font2,bg=self.greycolor,fg=self.whitecolor).grid(row=0,column=1,padx=50,pady=(100,10),sticky='nw')
        self.lblname=Label(self.dashframe,text=self.name.upper(),font=self.font2,bg=self.greycolor,fg=self.greencolor)
        self.lblname.grid(row=0,column=2,padx=50,pady=(100,10),sticky='nw')
        Label(self.dashframe,text='EMAIL ADDRESS:',font=self.font2,bg=self.greycolor,fg=self.whitecolor).grid(row=1,column=1,padx=50,sticky='nw')
        self.lblemail = Label(self.dashframe, text=self.email.upper(), font=self.font2,
                             bg=self.greycolor, fg=self.greencolor)
        self.lblemail.grid(row=1, column=2,padx=50,sticky='nw')
        Label(self.dashframe,text='MOBILE NUMBER:',font=self.font2,bg=self.greycolor,fg=self.whitecolor).grid(row=2,column=1,padx=50,pady=10,sticky='nw')
        self.lblphone = Label(self.dashframe, text=self.phonemum.upper(), font=self.font2,
                             bg=self.greycolor, fg=self.greencolor)
        self.lblphone.grid(row=2, column=2, pady=10,padx=50,sticky='nw')
        Label(self.dashframe, text='', bg=self.greencolor).grid(row=3,columnspan=3, column=1, pady=200,padx=200)


        #Report crime section
        self.reportframe = Frame(self.master, bg=self.greycolor, width=900, height=470)
        # self.reportframe.grid(row=1, column=1,sticky='nsew')
        Label(self.reportframe,text='R E P O R T  C R I M E', bg=self.greycolor,font=self.font1,
              fg=self.whitecolor).grid(row=0,column=0,columnspan=3,padx=32,pady=(25,10),sticky=NW)
        Label(self.reportframe, text='D A T E  O F  C R I M E :', bg=self.greycolor, font=self.font2,fg=self.whitecolor).grid(row=1,column=0,padx=(32,3),pady=10,sticky=NW)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TCombobox',fieldbackground=self.greencolor, background=self.greencolor, foreground=self.whitecolor)
        style.map('TCombobox', fieldbackground=[('readonly', self.greencolor)])
        style.map('TCombobox', selectbackground=[('readonly', self.greencolor)])
        self.cal = DateEntry(self.reportframe,selectmode='day',font=self.font2, year=2022)
        self.cal['state']='readonly'
        self.cal.grid(row=1,column=1,sticky=NW,pady=10)
        self.lbl_location=Label(self.reportframe,text='L O C A T I O N  O F  C R I M E :',bg=self.greycolor,font=self.font2,fg=self.whitecolor)
        self.lbl_location.grid(row=2,column=0,columnspan=3,padx=32,pady=10,sticky=NW)
        Label(self.reportframe, text='S T A T E :', bg=self.greycolor, font=self.font2, fg=self.whitecolor).grid(row=3,column=0, padx=(32,3),pady=10,sticky=W)
        self.combo_state=ttk.Combobox(self.reportframe, value=self.states,font=self.font2, width=12)
        self.combo_state['state']='readonly'
        self.combo_state.set('STATES')
        self.combo_state.grid(row=3,column=1,pady=10,sticky=NW)
        Label(self.reportframe, text='A D D R E S S :', bg=self.greycolor, font=self.font2,fg=self.whitecolor).grid(row=4, column=0, padx=(32,3), pady=10, sticky=NW)
        # self.combo_state.bind("<<ComboboxSelected>>", comboclick)
        self.ent_address= Entry(self.reportframe, width='45', bg=self.greencolor, border=0, fg=self.whitecolor, font=self.font3)
        self.ent_address.grid(row=4, column=1, sticky=NW, pady=10)
        Label(self.reportframe, text='T Y P E  O F  C R I M E :', bg=self.greycolor, font=self.font2, fg=self.whitecolor).grid(
            row=5, column=0, padx=(32, 3), pady=10, sticky=NW)
        self.combo_crime=ttk.Combobox(self.reportframe, value=self.crimes,font=self.font2, width=25)
        self.combo_crime['state']='readonly'
        self.combo_crime.set('CRIMES')
        self.combo_crime.grid(row=5,column=1,pady=10,sticky=NW)
        Label(self.reportframe, text='D E S C R I P T I O N :', bg=self.greycolor, font=self.font2, fg=self.whitecolor).grid(
            row=6, column=0, padx=(32, 3), pady=10, sticky=NW)
        self.ent_desc=Entry(self.reportframe,width='70', bg=self.greencolor, border=0, fg=self.whitecolor, font=self.font3)
        self.ent_desc.grid(row=6, column=1, sticky=NW, pady=10,columnspan=3)
        self.uploadevdc = Button(self.reportframe, text='UPLOAD EVIDENCE', cursor='hand2',  bg=self.lightgreycolor,
                             fg=self.whitecolor, border=0, font=self.font3,command=self.uploadevidence)
        self.uploadevdc.grid(row=7, column=0, sticky=W,padx=33, pady=(10,0))
        self.rprt = Button(self.reportframe, text='Report', cursor='hand2', width=9, bg=self.greencolor,
                               fg=self.whitecolor, border=0, font=self.font3, command=self.submitreport)
        self.rprt.grid(row=8, column=3, sticky=W, padx=(130,0), pady=(0,50))


        # view reports history section
        self.historyframe = Frame(self.master,bg=self.greycolor, width=900, height=470)
        # self.historyframe.grid(row=1, column=1,sticky='nsew')
        Label(self.historyframe, text='C R I M E  R E P O R T  H I S T O R Y', bg=self.greycolor, font=self.font1,
              fg=self.whitecolor).grid(row=0, column=0, padx=32, pady=(25, 10), sticky=NW)
        self.treeframe=Frame(self.historyframe, bg=self.greycolor, width=830, height=400)
        self.treeframe.grid(row=1, column=0, columnspan=2, padx=32, pady=(25, 200), sticky=NW)
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,font=self.font4)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading",borderwidth=1,background=self.lightergreycolor,relief='flat',
                        font=self.font2)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea',{'sticky': 'nswe'})])  # Remove the borders
        treescroll = Scrollbar(self.treeframe)
        treescroll.pack(side=RIGHT, fill=Y)
        treescroll2 = Scrollbar(self.treeframe, orient='horizontal')
        treescroll2.pack(side=BOTTOM, fill=X)
        self.historytree = ttk.Treeview(self.treeframe, height=10, xscrollcommand=treescroll2.set,yscrollcommand=treescroll.set,
                                        style="mystyle.Treeview", selectmode='browse')
        self.historytree.pack(fill=X)
        treescroll.config(command=self.historytree.yview)
        treescroll2.config(command=self.historytree.xview)
        self.historytree['columns'] = ("crimeID", "Date of crime", "State", "Address","Crime","Description","Status")
        self.historytree.column("#0", width=0, stretch=NO)
        self.historytree.column("crimeID", anchor=W, width=60, minwidth=100)
        self.historytree.column("Date of crime", anchor=W, width=80,minwidth=100)
        self.historytree.column("State", anchor=W, width=100,minwidth=100)
        self.historytree.column("Address", anchor=W, width=140,minwidth=150)
        self.historytree.column("Crime", anchor=W, width=120,minwidth=200)
        self.historytree.column("Description", anchor=W, width=250,minwidth=300)
        self.historytree.column("Status", anchor=W, width=60,minwidth=100)

        self.historytree.heading("#0", text="", anchor=W)
        self.historytree.heading("crimeID", text="crimeID", anchor=W)
        self.historytree.heading("Date of crime", text="Date", anchor=W)
        self.historytree.heading("State", text="State", anchor=W)
        self.historytree.heading("Address", text="Address", anchor=W)
        self.historytree.heading("Crime", text="Crime", anchor=W)
        self.historytree.heading("Description", text="Description", anchor=W)
        self.historytree.heading("Status", text="Status", anchor=W)
        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM crime_data WHERE email=? and status=?",[(self.email.lower()),("CONCLUDED")])
        records=cursor.fetchall()
        conn.commit()
        conn.close()
        self.count=0
        for record in records:
            self.historytree.insert(parent='',index='end',iid=self.count, values=(record[0],record[1],record[2],record[3],record[4],record[5],record[8]))
            self.count += 1

        # view reports status section
        self.statusframe = Frame(self.master, bg=self.greycolor, width=900, height=470)
        # self.statusframe.grid(row=1, column=1,sticky='nsew')
        Label(self.statusframe, text='R E P O R T  S T A T U S', bg=self.greycolor, font=self.font1,
              fg=self.whitecolor).grid(row=0, column=0, padx=32, pady=(25, 10), sticky=NW)
        self.treeframe2 = Frame(self.statusframe, bg=self.greycolor, width=830, height=400)
        self.treeframe2.grid(row=1, column=0, columnspan=2, padx=32, pady=(25, 200), sticky=NW)
        treescrollx = Scrollbar(self.treeframe2)
        treescrollx.pack(side=RIGHT, fill=Y)
        treescrolly = Scrollbar(self.treeframe2, orient='horizontal')
        treescrolly.pack(side=BOTTOM, fill=X)
        self.statustree = ttk.Treeview(self.treeframe2, height=10, yscrollcommand=treescrollx.set,xscrollcommand=treescrolly.set,
                                        style="mystyle.Treeview", selectmode='browse')
        self.statustree.pack(fill=X)
        treescrollx.config(command=self.statustree.yview)
        treescrolly.config(command=self.statustree.xview)
        self.statustree['columns'] = (
        "crimeID", "Date of crime", "State", "Address", "Crime", "Description", "Status")
        self.statustree.column("#0", width=0, stretch=NO)
        self.statustree.column("crimeID", anchor=W, width=60, minwidth=100)
        self.statustree.column("Date of crime", anchor=W, width=80,minwidth=100)
        self.statustree.column("State", anchor=W, width=100,minwidth=100)
        self.statustree.column("Address", anchor=W, width=140,minwidth=150)
        self.statustree.column("Crime", anchor=W, width=120,minwidth=200)
        self.statustree.column("Description", anchor=W, width=250,minwidth=300)
        self.statustree.column("Status", anchor=W, width=60,minwidth=100)

        self.statustree.heading("#0", text="", anchor=W)
        self.statustree.heading("crimeID", text="crimeID", anchor=W)
        self.statustree.heading("Date of crime", text="Date", anchor=W)
        self.statustree.heading("State", text="State", anchor=W)
        self.statustree.heading("Address", text="Address", anchor=W)
        self.statustree.heading("Crime", text="Crime", anchor=W)
        self.statustree.heading("Description", text="Description", anchor=W)
        self.statustree.heading("Status", text="Status", anchor=W)
        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM crime_data WHERE email=? and status!=?",
                       [(self.email.lower()), ("CONCLUDED")])
        records2 = cursor.fetchall()
        conn.commit()
        conn.close()
        self.counter = 0
        for record2 in records2:
            self.statustree.insert(parent='', index='end', iid=self.counter, values=(
            record2[0], record2[1], record2[2], record2[3], record2[4], record2[5], record2[8]))
            self.counter+=1



        #edit profile section
        self.editframe = Frame(self.master,bg=self.greycolor, width=900, height=470)
        # self.editframe.grid(row=1, column=1,sticky='nsew')
        self.lbl_fullname = Label(self.editframe, text='FULL NAME', bg=self.greycolor, fg=self.whitecolor,
                                  font=self.font2)
        self.lbl_fullname.grid(row=1, column=0, sticky=W, padx=32,pady=(60,0),columnspan=2)
        self.ent_fullname = Entry(self.editframe, width='45',bg=self.greycolor, border=0, fg=self.whitecolor,
                                  font=self.font4)
        self.ent_fullname.grid(row=2, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.editframe, width=350, height=1, bg=self.lightgreycolor).grid(row=3, column=0, sticky=W, padx=35,columnspan=2)
        Label(self.editframe, text='', bg=self.greycolor).grid(row=4, column=0, padx=180,columnspan=2)
        self.lbl_number = Label(self.editframe, text='PHONE NUMBER', bg=self.greycolor, fg=self.whitecolor,
                                font=self.font2)
        self.lbl_number.grid(row=5, column=0, sticky=W, padx=32,columnspan=2)
        self.ent_number = Entry(self.editframe, width='45',text=self.phonemum, bg=self.greycolor, border=0, fg=self.whitecolor,
                                font=self.font4)
        self.ent_number.grid(row=6, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.editframe, width=350, height=1, bg=self.lightgreycolor).grid(row=7, column=0, sticky=W, padx=35,columnspan=2)
        Label(self.editframe, text='', bg=self.greycolor).grid(row=8, column=0, padx=180,columnspan=2)
        self.lbl_password = Label(self.editframe, text='ENTER CURRENT PASSWORD', bg=self.greycolor, fg=self.whitecolor, font=self.font2)
        self.lbl_password.grid(row=9, column=0, sticky=W, padx=32,columnspan=2)
        self.ent_password = Entry(self.editframe, width='45',show='*', bg=self.greycolor, border=0, fg=self.whitecolor,
                              font=self.font4)
        self.ent_password.grid(row=10, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.editframe, width=350, height=1, bg=self.lightgreycolor).grid(row=11, column=0, sticky=W, padx=35,columnspan=2)
        Label(self.editframe, text='', bg=self.greycolor).grid(row=12, column=0, padx=180,columnspan=2)
        self.lbl_newpass = Label(self.editframe, text='ENTER NEW PASSWORD', bg=self.greycolor, fg=self.whitecolor,
                                  font=self.font2)
        self.lbl_newpass.grid(row=13, column=0, sticky=W, padx=32,columnspan=2)
        self.ent_newpass = Entry(self.editframe, width='45', show='*', bg=self.greycolor, border=0, fg=self.whitecolor,
                                  font=self.font4)
        self.ent_newpass.grid(row=14, column=0, sticky=W, padx=35, columnspan=2)
        Frame(self.editframe, width=350, height=1, bg=self.lightgreycolor).grid(row=15, column=0, sticky=W, padx=35,columnspan=2)
        Label(self.editframe, text='', bg=self.greycolor).grid(row=16, column=0, padx=180,columnspan=2)
        self.uploadbtn = Button(self.editframe, text='UPLOAD PROFILE PICTURE', cursor='hand2',  bg=self.lightgreycolor,
                             fg=self.whitecolor, border=0, font=self.font3,command=self.uploadphoto)
        self.uploadbtn.grid(row=17, column=0, sticky=E,padx=33, pady=15)
        self.resetbtn = Button(self.editframe, text='Reset', cursor='hand2', width=9, bg='#A5494F',
                             fg=self.whitecolor, border=0, font=self.font3, command=self.reset)
        self.resetbtn.grid(row=18, column=0, sticky=W, padx=(33,0), pady=(15,31))
        self.submitbtn = Button(self.editframe, text='Submit', cursor='hand2', width=9, bg=self.greencolor,
                             fg=self.whitecolor, border=0, font=self.font3,command=self.submit)
        self.submitbtn.grid(row=18, column=1, sticky=E,padx=50, pady=(15,31))
        self.submitbtn.bind('<Enter>', lambda e: self.on_enter(e, 3))
        self.submitbtn.bind('<Leave>', lambda e: self.on_leave(e, 3))
        self.resetbtn.bind('<Enter>', lambda e: self.on_enter(e, 1))
        self.resetbtn.bind('<Leave>', lambda e: self.on_leave(e, 1))
        self.uploadbtn.bind('<Enter>', lambda e: self.on_enter(e, 2))
        self.uploadbtn.bind('<Leave>', lambda e: self.on_leave(e, 2))


    def reset(self):
        self.ent_fullname.delete(0, END)
        self.ent_number.delete(0, END)
        self.ent_password.delete(0, END)
        self.ent_newpass.delete(0, END)
        self.ent_fullname.insert(0, self.name)
        self.ent_number.insert(0, self.phonemum)

    def submit(self):

        if self.ent_password.get() == '':
            messagebox.showerror('ERROR', 'Password Required')

        elif self.ent_newpass.get()=='':
            try:
                conn = sqlite3.connect("user_data2.db")
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM user_details WHERE email=? AND password=?",
                               [(self.email.lower()), (self.ent_password.get())])
                results = cursor.fetchall()
                if results:
                    cursor.execute("UPDATE user_details SET name=?,phone=? WHERE email=?", [(self.ent_fullname.get()),(self.ent_number.get()),(self.email.lower())])
                    messagebox.showinfo('HURRAY', 'Details updated successfully')
                    self.lbl_name.config(text=f'W E L C O M E\n{self.ent_fullname.get().upper()}')
                    self.lblname.config(text=self.ent_fullname.get().upper())
                    self.lblphone.config(text=self.ent_number.get())
                    self.ent_password.delete(0, END)
                    self.ent_newpass.delete(0, END)
                    conn.commit()
                    conn.close()
                else:
                    messagebox.showerror('ERROR', 'Incorrect Password')
            except:
                messagebox.showerror('ERROR', 'failed to add to database')

        elif self.ent_newpass.get() != '':
            try:
                conn = sqlite3.connect("user_data2.db")
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM user_details WHERE email=? AND password=?",
                               [(self.email.lower()), (self.ent_password.get())])
                results = cursor.fetchall()
                if results:
                    cursor.execute("UPDATE user_details SET name=?,phone=?,password=? WHERE email=?",
                                   [(self.ent_fullname.get()), (self.ent_number.get()), (self.ent_newpass.get()),
                                    (self.email.lower())])
                    messagebox.showinfo('HURRAY', 'Details updated successfully')
                    self.lbl_name.config(text=f'W E L C O M E\n{self.ent_fullname.get().upper()}')
                    self.lblname.config(text=self.ent_fullname.get().upper())
                    self.lblphone.config(text=self.ent_number.get())
                    self.ent_password.delete(0, END)
                    self.ent_newpass.delete(0, END)
                    conn.commit()
                    conn.close()
                else:
                    messagebox.showerror('ERROR', 'Incorrect Password')
            except:
                messagebox.showerror('ERROR', 'failed to add to database')

    def submitreport(self):
        if self.combo_state.get()=='STATES' or self.cal.get()=='' or self.combo_crime.get()=='CRIMES' or self.ent_address.get()=='' or self.ent_desc.get()=='':
            messagebox.showerror('ERROR', 'All fields are required')
            # print('some fields not filled')
        else:
            try:
                conn=sqlite3.connect("user_data2.db")
                cursor=conn.cursor()
                stmt="INSERT INTO crime_data(date,state,address,crime,description,email,evidence,status) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                entries=[(self.cal.get(),self.combo_state.get(),self.ent_address.get(),self.combo_crime.get(),self.ent_desc.get(), self.email.lower(),self.evdnc,"PENDING")]
                cursor.executemany(stmt,entries)
                conn.commit()
                cursor.execute("SELECT rowid, * FROM crime_data WHERE email=? and status!=?", [(self.email.lower()),("CONCLUDED")])
                records = cursor.fetchall()
                for record in records:
                    rowid=record[0]
                self.statustree.insert(parent='', index='end', iid=self.counter, values=(rowid,
                self.cal.get(), self.combo_state.get(), self.ent_address.get(), self.combo_crime.get(), self.ent_desc.get(),"PENDING"))
                self.counter += 1
                conn.close()
                self.uploadevdc.config(bg=self.lightgreycolor)
                self.ent_address.delete(0, END)
                self.ent_desc.delete(0, END)
                self.combo_state.set('STATES')
                self.combo_crime.set('CRIMES')
                messagebox.showinfo('success!','report successful ')
            except:
                messagebox.showerror('error','no evidence uploaded')



    def uploadevidence(self):
        try:
            self.getevidence=filedialog.askopenfilename(title="SELECT IMAGE",filetypes=(("jpg","*jpg"),("jpeg","*jpeg"),("png","*.png"),("Allfile","*.*")))
            if self.getevidence:
                self.uploadevdc.config(bg=self.greencolor)
                with open(self.getevidence,'rb') as f:
                    self.evdnc=f.read()
            else:
                messagebox.showerror('ERROR', 'No image selected')
        except:
            messagebox.showerror('ERROR', 'No image selected')


    def uploadphoto(self):
        try:
            self.getimage=filedialog.askopenfilename(title="SELECT IMAGE",filetypes=(("jpg","*jpg"),("jpeg","*jpeg"),("png","*.png"),("Allfile","*.*")))
            self.image=Image.open(self.getimage)
            resized=self.image.resize((128,128))
            self.newpic=ImageTk.PhotoImage(resized)
            self.picture.config(image=self.newpic)
            try:
                with open(self.getimage,'rb') as f:
                    m=f.read()

                conn = sqlite3.connect("user_data2.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE user_details SET picture=? WHERE email=?", [(m),(self.email.lower())])
                conn.commit()
                conn.close()
                messagebox.showinfo('HURRAY!!', 'Image added successfully!')
            except:
                messagebox.showerror('ERROR', 'failed to add to database')
        except:
            messagebox.showerror('ERROR', 'No image selected')
    def display(self):
        try:
            conn = sqlite3.connect("user_data2.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_details WHERE email=?", [(self.email.lower())])
            record = cursor.fetchall()
            for row in record:
                if row[4]!=None:
                    self.photo=row[4]
                    self.profilepic = "" + self.name + ".jpg"
                    with open(self.profilepic,'wb') as f:
                        f.write(self.photo)
                        conn.close()
                else:
                    self.profilepic='admin.png'
        except:
                messagebox.showerror('ERROR', 'failed to add to database')

    def logout(self):
        self.master.destroy()
        self.master.master.deiconify()

    def on_enter(self,e,n):
        if n==0:
            self.logout.config(background=self.lightgreycolor,foreground=self.greencolor)
        elif n==1:
            self.resetbtn.config(background='pink',foreground='#A5494F')
        elif n==2:
            self.uploadbtn.config(background=self.greencolor,foreground=self.lightgreycolor)
        elif n==3:
            self.submitbtn.config(background=self.lightgreycolor,foreground=self.greencolor)
    def on_leave(self,e,n):
        if n==0:
            self.logout.config(background=self.greencolor,foreground=self.greycolor)
        elif n==1:
            self.resetbtn.config(background='#A5494F',foreground=self.whitecolor)
        elif n==2:
            self.uploadbtn.config(background=self.lightgreycolor,foreground=self.whitecolor)
        elif n==3:
            self.submitbtn.config(background=self.greencolor,foreground=self.whitecolor)

    def on_enter2(self,e,n):
        if self.var[n]:
            self.btns[n].config(background=self.lightgreycolor,foreground=self.greencolor)
            self.btns2[n].config(background=self.lightgreycolor,foreground=self.greencolor)
        else:
            self.btns[n].config(background=self.lightgreycolor,foreground=self.greencolor)
            self.btns2[n].config(background=self.lightgreycolor, foreground=self.whitecolor)

    def on_leave2(self,e,n):
        if self.var[n]:
            self.btns[n].config(background=self.darkgreycolor,foreground=self.greencolor)
            self.btns2[n].config(background=self.greencolor, foreground=self.whitecolor)
        else:
            self.btns[n].config(background=self.greencolor,foreground=self.whitecolor)
            self.btns2[n].config(background=self.greycolor, foreground=self.greencolor)

    def cmd1(self,n):
        for i in range(len(self.btns)):
            self.btns[i].config(fg=self.whitecolor,bg=self.greencolor)
            self.btns2[i].config(fg=self.greencolor, bg=self.greycolor)
            # self.btns2[i].config(height=1)
            self.var[i]=False
            self.f[i].config(bg=self.greycolor)
        self.btns[n].config(fg=self.greencolor,bg=self.darkgreycolor)
        self.var[n]=True
        self.btns2[n].config(fg=self.whitecolor,bg=self.greencolor)
        # self.btns2[n].config(height=2)
        self.f[n].config(bg=self.greencolor)
        if self.var[0]:
            self.editframe.grid_forget()
            self.reportframe.grid_forget()
            self.historyframe.grid_forget()
            self.statusframe.grid_forget()
            self.dashframe.grid(row=1, column=1, sticky='nsew')
        elif self.var[1]:
            self.editframe.grid_forget()
            self.dashframe.grid_forget()
            self.historyframe.grid_forget()
            self.statusframe.grid_forget()
            self.reportframe.grid(row=1, column=1, sticky='nsew')
        elif self.var[2]:
            self.editframe.grid_forget()
            self.reportframe.grid_forget()
            self.dashframe.grid_forget()
            self.statusframe.grid_forget()
            self.historyframe.grid(row=1, column=1, sticky='nsew')
        elif self.var[3]:
            self.editframe.grid_forget()
            self.reportframe.grid_forget()
            self.dashframe.grid_forget()
            self.historyframe.grid_forget()
            self.statusframe.grid(row=1, column=1, sticky='nsew')
        elif self.var[4]:
            self.ent_fullname.delete(0, END)
            self.ent_number.delete(0, END)
            self.ent_password.delete(0, END)
            self.ent_newpass.delete(0, END)
            self.ent_fullname.insert(0, self.name)
            self.ent_number.insert(0, self.phonemum)
            self.dashframe.grid_forget()
            self.reportframe.grid_forget()
            self.historyframe.grid_forget()
            self.statusframe.grid_forget()
            self.editframe.grid(row=1, column=1, sticky='nsew')


    def slideshow(self):
        if self.slide == 5:
            self.slide = 1
        if self.slide == 1:
            self.pfp.config(image=self.img1)
        elif self.slide == 2:
            self.pfp.config(image=self.img2)
        elif self.slide == 3:
            self.pfp.config(image=self.img3)
        elif self.slide == 4:
            self.pfp.config(image=self.img)
        self.slide += 1
        self.after(3000, self.slideshow)


class Admindashboard(Frame):
    def __init__(self, master):
        super(Admindashboard, self).__init__(master)
        self.master=master
        # self.place()
        # self.pack()
        self.grid()
        self.slide=0
        self.font1=f.Font(family='Yu Gothic UI Light', size=30)
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=15)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=20)
        self.greencolor = '#48BF91'
        self.greycolor = '#252D3B'
        self.lightgreycolor = '#51545e'
        self.lightergreycolor = '#DCDCDC'
        self.whitecolor='white'
        self.darkgreycolor='#363942'
        self.create_widgets()
        self.runner()
        self.runner1()
        self.runner2()
        self.runner3()
        self.gengraph()
        self.time()

    def create_widgets(self):
        self.bgf=Frame(self.master,width=1200,height=690,bg='#303A48')
        self.bgf.grid(row=0, column=0)
        self.frame1=Frame(self.bgf,width=300,height=650,bg=self.greycolor)
        self.frame1.grid(row=0,column=0,padx=30,pady=30,rowspan=2,sticky='nsew')
        self.img = ImageTk.PhotoImage(Image.open("admin.png"))
        self.img1 = ImageTk.PhotoImage(Image.open("dashicon.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("list-text.png"))
        self.img3 = ImageTk.PhotoImage(Image.open("refresh.png"))
        self.img4 = ImageTk.PhotoImage(Image.open("dashicon2.png"))
        self.img9 = ImageTk.PhotoImage(Image.open("list-text (1).png"))
        self.img10 = ImageTk.PhotoImage(Image.open("refresh (1).png"))
        Label(self.frame1,image=self.img,bg=self.greycolor).grid(row=0,column=0,padx=80,pady=15,sticky='nsew',columnspan=2)
        Label(self.frame1, font=self.font3, text='A D M I N I S T R A T O R', bg=self.greycolor,fg=self.greencolor).grid(row=1,column=0,columnspan=2)
        Frame(self.frame1, width=250, height=1, bg=self.greencolor).grid(row=2, column=0,columnspan=2,pady=3)
        self.clock=Label(self.frame1, bg=self.greycolor,fg=self.greencolor,font=self.font3)
        self.clock.grid(row=3, column=0,columnspan=2,pady=12)
        self.f1=Frame(self.frame1,width=6,height=41,bg=self.greencolor)
        self.f1.grid(row=4,column=0)
        self.f2 = Frame(self.frame1, width=6, height=41, bg=self.greycolor)
        self.f2.grid(row=5, column=0)
        self.f3 = Frame(self.frame1, width=6, height=41, bg=self.greycolor)
        self.f3.grid(row=6, column=0)
        self.dashboard=Button(self.frame1,image=self.img4,compound=LEFT,width=283,pady=7,text=' D A S H B O A R D\t\t',font=self.font2,cursor='hand2',border=0,bg=self.lightgreycolor,fg=self.greencolor, command=lambda :self.cmd(0))
        self.dashboard.grid(row=4,column=1,columnspan=2,sticky=NW)
        self.reports = Button(self.frame1,image=self.img2,compound=LEFT,width=283,pady=7, text=' R E P O R T S\t\t',font=self.font2,cursor='hand2',border=0,bg=self.greycolor,fg=self.whitecolor, command=lambda :self.cmd(1))
        self.reports.grid(row=5,column=1,sticky=NW)
        self.status = Button(self.frame1,image=self.img3,compound=LEFT,width=283,pady=7, text=' U P D A T E  S T A T U S\t', font=self.font2,cursor='hand2',border=0,bg=self.greycolor,fg=self.whitecolor, command=lambda :self.cmd(2))
        self.status.grid(row=6,column=1,sticky=NW)
        Label(self.frame1,bg=self.greycolor,text='').grid(row=7,column=0,columnspan=2,pady=97)
        self.logout=Button(self.frame1,width=36,pady=5,text='L O G O U T',bg=self.lightgreycolor,font=self.font2,border=0,cursor='hand2',fg=self.greencolor, command=self.logoutcmd)
        self.logout.grid(row=8,column=0,columnspan=2)
        self.dashboard.bind('<Enter>', lambda e: self.on_enter(e, 0))
        self.dashboard.bind('<Leave>', lambda e: self.on_leave(e, 0))
        self.reports.bind('<Enter>', lambda e: self.on_enter(e, 1))
        self.reports.bind('<Leave>', lambda e: self.on_leave(e, 1))
        self.status.bind('<Enter>', lambda e: self.on_enter(e, 2))
        self.status.bind('<Leave>', lambda e: self.on_leave(e, 2))


        self.img11 = ImageTk.PhotoImage(Image.open("cancel.png"))
        Button(self.bgf,image=self.img11, command=self.master.master.destroy,cursor='hand2',bg='#303A48',borderwidth=0).grid(row=0,column=2,padx=10,sticky=NE)


        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM crime_data")
        casenum = cursor.fetchall()
        self.casenums=len(casenum)
        cursor.execute("SELECT rowid, * FROM crime_data WHERE status==?", [("PENDING")])
        pendnum = cursor.fetchall()
        self.pendnums=len(pendnum)
        cursor.execute("SELECT rowid, * FROM crime_data WHERE status==?", [("INVESTIGATING")])
        invnum = cursor.fetchall()
        self.invnums=len(invnum)
        cursor.execute("SELECT rowid, * FROM crime_data WHERE status==?",[("CONCLUDED")])
        concnum = cursor.fetchall()
        self.concnums=len(concnum)
        conn.close()
        self.num=0
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0


        self.frame2 = Frame(self.bgf, width=820, height=180, bg=self.greycolor)
        self.frame2.grid(row=0, column=1, pady=30,sticky='nw')
        self.img5 = ImageTk.PhotoImage(Image.open("chart.png"))
        self.img7 = ImageTk.PhotoImage(Image.open("statistical.png"))
        Label(self.frame2, text='Total number of\ncases reported', font=self.font3, bg=self.greycolor,fg=self.whitecolor).grid(row=0, padx=(30,0), pady=(9,0), column=0)
        self.casenum= Label(self.frame2, text='0', font=self.font4, bg=self.greycolor,fg=self.greencolor)
        self.casenum.grid(row=1, column=0,pady=(0,35), padx=(30,0))
        Frame(self.frame2,bg=self.lightgreycolor,width=2,height=140).grid(row=0,column=1,rowspan=2,padx=23)
        Label(self.frame2, text='Total number of\n Pending cases ', font=self.font3, bg=self.greycolor,fg=self.whitecolor).grid(row=0, padx=10, pady=(9,0), column=2)
        self.pendnum= Label(self.frame2, text='0', font=self.font4, bg=self.greycolor,fg=self.greencolor)
        self.pendnum.grid(row=1, column=2,pady=(0,35))
        Frame(self.frame2,bg=self.lightgreycolor,width=2,height=140).grid(row=0,column=3,rowspan=2,padx=26)
        Label(self.frame2, text='Total number of\ncases under\n  Investigation  ', font=self.font3, bg=self.greycolor,fg=self.whitecolor).grid(row=0, padx=10, pady=(9,0), column=4)
        self.invnum= Label(self.frame2, text='0', font=self.font4, bg=self.greycolor,fg=self.greencolor)
        self.invnum.grid(row=1, column=4,pady=(0,35))
        Frame(self.frame2,bg=self.lightgreycolor,width=2,height=140).grid(row=0,column=5,rowspan=2,padx=20)
        Label(self.frame2, text='Total number of\n Concluded cases', font=self.font3, bg=self.greycolor,fg=self.whitecolor).grid(row=0, padx=(0,30), pady=(9,0), column=6)
        self.concnum= Label(self.frame2, text='0', font=self.font4, bg=self.greycolor,fg=self.greencolor)
        self.concnum.grid(row=1, column=6,pady=(0,35),padx=(0,30))




        self.frame3a = Frame(self.bgf, width=900, height=400, bg='#303A48')
        self.frame3a.grid(row=1, column=1, sticky='nw')



        # view reports section design
        self.viewreports = Frame(self.bgf, width=800, height=400, bg=self.greycolor)
        # self.viewreports.grid(row=1, column=1,columnspan=2, sticky='nw')
        self.img8 = ImageTk.PhotoImage(Image.open("upload.png"))
        Label(self.viewreports, text='R E P O R T S', bg=self.greycolor, font=self.font4,
              fg=self.whitecolor).pack(pady=(0,10))
        self.treeframe = Frame(self.viewreports, bg=self.greycolor, width=800, height=400)
        self.treeframe.pack()
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=self.font2)  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", borderwidth=1, background=self.lightergreycolor, relief='flat',
                        font=self.font2)  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        treescroll = Scrollbar(self.treeframe)
        treescroll.pack(side=RIGHT, fill=Y)
        treescroll2 = Scrollbar(self.treeframe, orient='horizontal')
        treescroll2.pack(side=BOTTOM, fill=X)
        self.reportstree = ttk.Treeview(self.treeframe, height=12, yscrollcommand=treescroll.set,xscrollcommand=treescroll2.set,
                                        style="mystyle.Treeview", selectmode='browse')
        self.reportstree.pack(fill=X)
        self.updatebtn=Button(self.viewreports, text='Update')
        self.updatebtn = Button(self.viewreports,image=self.img8,compound=LEFT,width=200,pady=7, text=' U P D A T E', font=self.font2,cursor='hand2',border=0,bg=self.greencolor,command=self.firstupdate,fg=self.whitecolor)
        self.updatebtn.pack(side=BOTTOM,pady=10)
        treescroll.config(command=self.reportstree.yview)
        self.reportstree['columns'] = ("crimeID","user", "Date of crime", "State", "Address", "Crime", "Description", "Status")
        self.reportstree.column("#0", width=0, stretch=NO)
        self.reportstree.column("crimeID", anchor=W, width=50, minwidth=100)
        self.reportstree.column("user", anchor=W, width=50,minwidth=200)
        self.reportstree.column("Date of crime", anchor=W, width=80,minwidth=100)
        self.reportstree.column("State", anchor=W, width=100,minwidth=100)
        self.reportstree.column("Address", anchor=W, width=120,minwidth=150)
        self.reportstree.column("Crime", anchor=W, width=140,minwidth=200)
        self.reportstree.column("Description", anchor=W, width=200,minwidth=300)
        self.reportstree.column("Status", anchor=W, width=60,minwidth=100)

        self.reportstree.heading("#0", text="", anchor=W)
        self.reportstree.heading("crimeID", text="crimeID", anchor=CENTER)
        self.reportstree.heading("user", text="User", anchor=CENTER)
        self.reportstree.heading("Date of crime", text="Date", anchor=CENTER)
        self.reportstree.heading("State", text="State", anchor=CENTER)
        self.reportstree.heading("Address", text="Address", anchor=CENTER)
        self.reportstree.heading("Crime", text="Crime", anchor=CENTER)
        self.reportstree.heading("Description", text="Description", anchor=CENTER)
        self.reportstree.heading("Status", text="Status", anchor=W)
        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM crime_data")
        records = cursor.fetchall()
        conn.commit()
        conn.close()
        self.count = 0
        for record in records:
            if self.count % 2 == 0:
                self.reportstree.insert(parent='', index='end', iid=self.count, values=(
                record[0],record[6], record[1], record[2], record[3], record[4], record[5], record[8]), tags=('even',))
                self.count += 1
            else:
                self.reportstree.insert(parent='', index='end', iid=self.count, values=(
                record[0],record[6], record[1], record[2], record[3], record[4], record[5], record[8]), tags=('odd',))
                self.count += 1
        treescroll2.configure(command=self.reportstree.xview)
        self.reportstree.tag_configure('even', background=self.greycolor)
        self.reportstree.tag_configure('odd', background=self.lightgreycolor)


        # update status frame design
        self.statusframe = Frame(self.bgf, width=810, height=400, bg=self.greycolor)
        # self.statusframe.grid(row=1, column=1, sticky='nw')

        Label(self.statusframe, text='U P D A T E  S T A T U S', bg=self.greycolor, font=self.font4,
              fg=self.whitecolor).grid(row=0,column=0,columnspan=3)

        self.search=Entry(self.statusframe,width=25,bg="#303A48",border=0,fg=self.lightergreycolor, font=self.font3)
        self.search.grid(row=1,column=1,pady=10,padx=(375,0),sticky=E)
        self.search.insert(0, 'Search crimeID')
        self.search.bind("<FocusIn>",self.placeholderin)
        self.search.bind("<FocusOut>", self.placeholderout)


        self.searchbtn=Button(self.statusframe,text="S E A R C H",border=0,cursor='hand2',bg=self.greencolor,fg=self.whitecolor,command=self.searchid,font=self.font2,width=10)
        self.searchbtn.grid(row=1,column=2,pady=10,sticky=W)

        self.statustreeframe = Frame(self.statusframe, bg=self.greycolor, width=800, height=400)
        self.statustreeframe.grid(row=2,column=0,columnspan=3,sticky=NW)
        self.btnback=Button(self.statusframe,text="R E T U R N",border=0,cursor='hand2',bg="#A5494F",fg=self.whitecolor,command= self.back,font=self.font2,width=10)
        self.btnback.grid(row=4,column=0,pady=13,padx=(10,0),sticky=W)
        self.evidencebtn=Button(self.statusframe,text="V I E W  E V I D E N C E",border=0,cursor='hand2',bg=self.greencolor,fg=self.whitecolor,command=self.evidenceshow,font=self.font2)
        self.evidencebtn.grid(row=4,column=1,pady=13,sticky=E,padx=5)
        self.btnupdate=Button(self.statusframe,text="U P D A T E",border=0,cursor='hand2',bg=self.greencolor,fg=self.whitecolor,command= self.secondupdate,font=self.font2,width=10)
        self.btnupdate.grid(row=4,column=2,pady=13,padx=(5,0),sticky=W)
        treescrolly = Scrollbar(self.statustreeframe)
        treescrolly.pack(side=RIGHT, fill=Y)
        treescrollx = Scrollbar(self.statustreeframe, orient='horizontal')
        treescrollx.pack(side=BOTTOM, fill=X)
        self.updatetree = ttk.Treeview(self.statustreeframe, height=10, xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set,
                                        style="mystyle.Treeview", selectmode='browse')
        self.updatetree.pack(fill=X)
        treescrolly.config(command=self.updatetree.yview)
        treescrollx.config(command=self.updatetree.xview)
        self.updatetree['columns'] = ("crimeID","user", "Date of crime", "State", "Address", "Crime", "Description","Evidence", "Status")
        self.updatetree.column("#0", width=0, stretch=NO)
        self.updatetree.column("crimeID", anchor=W, width=50, minwidth=100)
        self.updatetree.column("user", anchor=W, width=50,minwidth=200)
        self.updatetree.column("Date of crime", anchor=W, width=80,minwidth=100)
        self.updatetree.column("State", anchor=W, width=112,minwidth=100)
        self.updatetree.column("Address", anchor=W, width=100,minwidth=150)
        self.updatetree.column("Crime", anchor=W, width=100,minwidth=200)
        self.updatetree.column("Description", anchor=W, width=200,minwidth=300)
        self.updatetree.column("Evidence", anchor=W, width=50, minwidth=230)
        self.updatetree.column("Status", anchor=W, width=60,minwidth=140)

        self.updatetree.heading("#0", text="", anchor=W)
        self.updatetree.heading("crimeID", text="crimeID", anchor=W)
        self.updatetree.heading("user", text="User", anchor=W)
        self.updatetree.heading("Date of crime", text="Date", anchor=W)
        self.updatetree.heading("State", text="State", anchor=W)
        self.updatetree.heading("Address", text="Address", anchor=W)
        self.updatetree.heading("Crime", text="Crime", anchor=W)
        self.updatetree.heading("Description", text="Description", anchor=W)
        self.updatetree.heading("Evidence", text="Evidence", anchor=W)
        self.updatetree.heading("Status", text="Status", anchor=W)
        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM crime_data WHERE status!=?",[("CONCLUDED")])
        records2 = cursor.fetchall()
        conn.commit()
        conn.close()
        self.counter = 0

        for record2 in records2:
            self.photo="" + record2[6] + f"_{self.counter}.jpg"
            self.updatetree.insert(parent='', index='end', iid=self.counter, values=(
                record2[0],record2[6], record2[1], record2[2], record2[3], record2[4], record2[5],self.photo, record2[8]))
            self.counter += 1

        self.var=[True, False, False]
        self.btns=[self.dashboard,self.reports,self.status]
        self.imgs=[self.img1,self.img2,self.img3]
        self.imgs2=[self.img4,self.img9,self.img10]



    def gengraph(self):
        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        figure = Figure(figsize=(8.2, 2.2), dpi=100, facecolor='#252D3B')
        ax = figure.add_subplot(111)
        ax.set_facecolor('#252D3B')
        bar1 = FigureCanvasTkAgg(figure, master=self.frame3a)
        bar1.get_tk_widget().grid(row=1, column=0, columnspan=2)

        states = ['Lagos', 'FCT(ABUJA)', 'Rivers', 'Anambra', 'Delta', 'Ogun']
        reported_crimes = [10, 20, 16, 13, 12, 19]
        pending_crimes = [2, 1, 4, 5, 4, 1]
        invest_crimes = [1, 5, 4, 2, 7, 2]
        concluded_crimes = [2, 1, 5, 0, 4, 3]
        a = []
        b = []
        c = []
        d = []
        for state in range(len(states)):
            cursor.execute("SELECT * FROM crime_data WHERE status=? and state=?", [("CONCLUDED"), (states[state])])
            records2 = cursor.fetchall()
            a.append(len(records2))
        for state in range(len(states)):
            cursor.execute("SELECT * FROM crime_data WHERE status=? and state=?", [("PENDING"), (states[state])])
            records2 = cursor.fetchall()
            b.append(len(records2))
        for state in range(len(states)):
            cursor.execute("SELECT * FROM crime_data WHERE status=? and state=?", [("INVESTIGATING"), (states[state])])
            records2 = cursor.fetchall()
            c.append(len(records2))
        for state in range(len(states)):
            cursor.execute("SELECT * FROM crime_data WHERE state=?", [(states[state])])
            records2 = cursor.fetchall()
            d.append(len(records2))
        x_axis = np.arange(len(states))
        ax.bar(x_axis + 0.15, d, width=0.15, label='Total crimes reported')
        ax.bar(x_axis + 0.15 * 2, a, width=0.15, label='Total crimes conluded')
        ax.bar(x_axis + 0.15 * 3, c, width=0.15, label='Total crimes under investigation')
        ax.bar(x_axis + 0.15 * 4, b, width=0.15, label='Total crimes pending', color='#48BF91')
        ax.set_xticks(0.35 + x_axis)
        ax.set_xticklabels(states)
        # plt.xticks(0.35+x_axis, states)
        ax.set_xlabel('States', color=self.greencolor)
        ax.set_ylabel('Total crimes reported', color=self.greencolor)
        ax.set_title('CRIME RATE IN MAJOR CITIES', color=self.greencolor, font='Arial')
        ax.set_facecolor(self.greycolor)
        ax.spines['bottom'].set_color(self.whitecolor)
        ax.spines['left'].set_color(self.whitecolor)
        ax.spines['top'].set_color(self.greycolor)
        ax.spines['right'].set_color(self.greycolor)
        ax.tick_params(axis='x', colors=self.greencolor)
        ax.tick_params(axis='y', colors=self.greencolor)
        ax.grid(True, color=self.whitecolor, linestyle=':')
        ax.legend()

        linechart = Figure(figsize=(5.15, 2), dpi=75, facecolor=self.greycolor)
        cx = linechart.add_subplot(111)
        cx.set_title('LINE CHART REPRESENTATION', color=self.greencolor, font='Arial')
        cx.plot(states, d, label='reported')
        cx.plot(states, a, label='conluded')
        cx.plot(states, c, label='investigating')
        cx.plot(states, b, label='pending')
        cx.set_xlabel('States', color=self.greencolor)
        cx.set_ylabel('Total crimes reported', color=self.greencolor)
        cx.set_facecolor(self.greycolor)
        cx.spines['bottom'].set_color(self.whitecolor)
        cx.spines['left'].set_color(self.whitecolor)
        cx.spines['top'].set_color(self.greycolor)
        cx.spines['right'].set_color(self.greycolor)
        cx.tick_params(axis='x', colors=self.greencolor)
        cx.tick_params(axis='y', colors=self.greencolor)
        cx.grid(True, color='white', linestyle=':')
        cx.legend()
        chart1 = FigureCanvasTkAgg(linechart, master=self.frame3a)
        chart1.draw()
        chart1.get_tk_widget().grid(row=0, column=1, pady=(0, 30), sticky=NE, padx=(15, 0))

        piechart = Figure(figsize=(5.15, 2), dpi=75, facecolor=self.greycolor)
        bx = piechart.add_subplot(111)
        total = self.casenums - sum(d)
        d.append(total)
        states.append("Others")
        exploded = [0, 0, 0, 0.2, 0, 0, 0.2]
        patches, texts, autotexts = bx.pie(d, labels=states, explode=exploded, autopct='%1.1f%%')
        bx.set_title('HIGHEST CRIME RATES', color=self.greencolor, font='Arial')
        for text in texts:
            text.set_color(self.greencolor)

        for autotext in autotexts:
            autotext.set_color(self.whitecolor)
        bx.axis('equal')
        chart = FigureCanvasTkAgg(piechart, master=self.frame3a)
        chart.draw()
        chart.get_tk_widget().grid(row=0, column=0, pady=(0, 30), padx=(0, 15), sticky=NW)
        conn.close()




    def time(self):
        self.a=strftime("%H : %M : %S")
        self.clock.config(text=self.a)
        self.clock.after(1000,self.time)

    def cmd(self,n):
        if n==0:
            self.viewreports.grid_forget()
            self.statusframe.grid_forget()
            self.frame3a.grid(row=1, column=1, sticky='nw')
            self.dashboard.config(image=self.img4, bg=self.lightgreycolor,fg=self.greencolor)
            self.reports.config(image=self.img2, bg=self.greycolor,fg=self.whitecolor)
            self.status.config(image=self.img3,bg=self.greycolor,fg=self.whitecolor)
            self.f1.config(bg=self.greencolor)
            self.f2.config(bg=self.greycolor)
            self.f3.config(bg=self.greycolor)
            self.var[0] = True
            self.var[1] = False
            self.var[2] = False
        elif n==1:
            self.frame3a.grid_forget()
            self.statusframe.grid_forget()
            self.viewreports.grid(row=1, column=1, sticky='nw')
            self.dashboard.config(image=self.img1, bg=self.greycolor,fg=self.whitecolor)
            self.reports.config(image=self.img9, bg=self.lightgreycolor,fg=self.greencolor)
            self.status.config(image=self.img3, bg=self.greycolor,fg=self.whitecolor)
            self.f1.config(bg=self.greycolor)
            self.f2.config(bg=self.greencolor)
            self.f3.config(bg=self.greycolor)
            self.var[0] = False
            self.var[1] = True
            self.var[2] = False
        elif n==2:
            self.frame3a.grid_forget()
            self.viewreports.grid_forget()
            self.statusframe.grid(row=1, column=1, sticky='nw')
            self.dashboard.config(image=self.img1, bg=self.greycolor, fg=self.whitecolor)
            self.reports.config(image=self.img2, bg=self.greycolor, fg=self.whitecolor)
            self.status.config(image=self.img10, bg=self.lightgreycolor, fg=self.greencolor)
            self.f1.config(bg=self.greycolor)
            self.f2.config(bg=self.greycolor)
            self.f3.config(bg=self.greencolor)
            self.var[0] = False
            self.var[1] = False
            self.var[2] = True

    def runner(self):
        if self.num < self.casenums:
            self.num += 1
            self.casenum.config(text=f'{self.num}')
        self.after(10, self.runner)

    def runner1(self):
        if self.num1 < self.pendnums:
            self.num1 += 1
            self.pendnum.config(text=f'{self.num1}')
            self.after(20, self.runner1)
    def runner2(self):
        if self.num2 < self.invnums:
            self.num2 += 1
            self.invnum.config(text=f'{self.num2}')
            self.after(20, self.runner2)
    def runner3(self):
        if self.num3 < self.concnums:
            self.num3 += 1
            self.concnum.config(text=f'{self.num3}')
            self.after(20, self.runner3)

    def on_enter(self, e, n):
        if self.var[n]:
            self.btns[n].config(image=self.imgs[n], background=self.greencolor, foreground=self.whitecolor)

        else:
            self.btns[n].config(image=self.imgs[n],background=self.greencolor, foreground=self.whitecolor)


    def on_leave(self, e, n):
        if self.var[n]:
            self.btns[n].config(image=self.imgs2[n],background=self.lightgreycolor, foreground=self.greencolor)

        else:
            self.btns[n].config(image=self.imgs[n],background=self.greycolor, foreground=self.whitecolor)

    def placeholderin(self,e):
        self.search.delete(0, END)

    def placeholderout(self,e):
        if self.search.get()=='':
            self.search.insert(0,'Search crimeID')

    def back(self):

        conn = sqlite3.connect("user_data2.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, * FROM crime_data WHERE status!=?",[("CONCLUDED")])
        records2 = cursor.fetchall()
        conn.commit()
        conn.close()
        self.counter = 0
        for items in self.updatetree.get_children():
            self.updatetree.delete(items)
        for record2 in records2:
            self.photo = "" + record2[6] + f"_{self.counter}.jpg"
            self.updatetree.insert(parent='', index='end', iid=self.counter, values=(
                record2[0],record2[6], record2[1], record2[2], record2[3], record2[4], record2[5],self.photo, record2[8]))
            self.counter += 1

    def searchid(self):
        if self.search.get()=="":
            messagebox.showerror("ERROR","pls input column id")
        else:
            try:
                self.counter = 0
                conn = sqlite3.connect("user_data2.db")
                cursor = conn.cursor()
                cursor.execute("SELECT rowid, * FROM crime_data WHERE rowid=?", [(self.search.get())])
                records2 = cursor.fetchall()
                if records2:
                    for items in self.updatetree.get_children():
                        self.updatetree.delete(items)
                    for record2 in records2:
                        self.photo = "evidence.jpg"
                        self.updatetree.insert(parent='', index='end', iid=self.counter, values=(
                            record2[0], record2[6], record2[1], record2[2], record2[3], record2[4], record2[5],
                            self.photo, record2[8]))
                        self.counter += 1
                    conn.commit()
                    conn.close()
                else:
                    messagebox.showerror("ERROR","Record not found")
                    conn.commit()
                    conn.close()
            except:
                messagebox.showerror("ERROR","Record not found")

    def firstupdate(self):
        try:
            conn = sqlite3.connect("user_data2.db")
            cursor = conn.cursor()
            selected = self.reportstree.focus()
            values = self.reportstree.item(selected, 'values')
            cursor.execute("SELECT rowid, * FROM crime_data WHERE rowid=?",[(values[0])])
            records = cursor.fetchall()
            for items in self.updatetree.get_children():
                self.updatetree.delete(items)
            for record in records:
                self.photo = 'evidence.jpg'
                self.updatetree.insert(parent='', index='end', iid=0, values=(
                    record[0], record[6], record[1], record[2], record[3], record[4], record[5],
                    self.photo, record[8]))
            conn.commit()
            conn.close()
            self.cmd(2)
        except:
            messagebox.showerror('ERROR', 'No records selected')

    def secondupdate(self):
        try:
            conn = sqlite3.connect("user_data2.db")
            cursor = conn.cursor()
            selected = self.updatetree.focus()
            values = self.updatetree.item(selected, 'values')
            if values[8] == 'PENDING':
                cursor.execute("UPDATE crime_data SET status=? WHERE rowid=?",[("INVESTIGATING"),(values[0])])
                self.updatetree.item(selected, text='', values=(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],'INVESTIGATING'))
                self.num1=0
                self.num2=0
                self.pendnums-=1
                self.invnums+=1
                self.runner1()
                self.runner2()
                conn.commit()
                conn.close()
            elif values[8]=='INVESTIGATING':
                cursor.execute("UPDATE crime_data SET status=? WHERE rowid=?",[("CONCLUDED"),(values[0])])
                self.updatetree.item(selected, text='', values=(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],'INVESTIGATING'))
                self.updatetree.item(selected, text='', values=(
                values[0], values[1], values[2], values[3], values[4], values[5], values[6],values[7], 'CONCLUDED'))
                self.num2=0
                self.num3=0
                self.invnums-=1
                self.concnums+=1
                self.runner2()
                self.runner3()
                conn.commit()
                conn.close()
            elif values[8]=='CONCLUDED':
                messagebox.showerror('ERROR', 'Case already concluded')

                conn.commit()
                conn.close()
        except:
            messagebox.showerror('ERROR', 'No records selected')

    def logoutcmd(self):
        self.master.destroy()
        self.master.master.deiconify()
    def evidenceshow(self):
        try:
            selected = self.updatetree.focus()
            values = self.updatetree.item(selected, 'values')
            conn = sqlite3.connect("user_data2.db")
            cursor = conn.cursor()
            cursor.execute("SELECT rowid, * FROM crime_data WHERE rowid=?", [(values[0])])
            details=cursor.fetchall()
            with open("evidence.jpg", 'wb') as f:
                f.write(details[0][7])
            self.evid = Toplevel(self.master)
            self.evid.resizable(0, 0)
            self.evid.configure(bg = '#303A48')
            # self.evid.overrideredirect(1)
            app_width = 512
            app_height = 512
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            self.evid.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            self.app = Evidwin(self.evid,"evidence.jpg")
        except:
            messagebox.showerror('ERROR','No records selected')


class Evidwin(Frame):
    def __init__(self, master,picture):
        super(Evidwin, self).__init__(master)
        self.master = master
        self.pic = ImageTk.PhotoImage(Image.open(picture).resize((512, 512)))
        self.frame = Frame(self.master, bg='#303A48')
        self.img=Label(self.frame, image=self.pic,bg='#303A48')
        self.img.pack()
        self.frame.pack()




# if __name__=="__main__":
def login():
    root = Tk()
    root.resizable(0, 0)
    # root.title("C R I M E  R E P O R T I N G  S Y S T E M")
    app_width = 700
    app_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    root.overrideredirect(1)
    app = Application(root)
    app.mainloop()
    # login()


