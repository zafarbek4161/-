from Detector import main_app
from create_classifier import train_classifer
from create_dataset import start_capture
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox,PhotoImage
#from PIL import ImageTk, Image
#from gender_prediction import emotion,ageAndgender

names = set()


class MainUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        global names
        with open("nameslist.txt", "r") as f:
            x = f.read()
            z = x.rstrip().split(" ")
            for i in z:
                names.add(i)
        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold")
        self.title("Распознавания лица")
        self.resizable(False, False)
        self.geometry("920x700")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.active_name = None
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=5, column=2, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

    def on_closing(self):

        if messagebox.askokcancel("Выход", "Вы уверены?"):
            global names
            f =  open("nameslist.txt", "a+")
            for i in names:
                    f.write(i+" ")
            self.destroy()


class StartPage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            #load = Image.open("homepagepic.png")
            #load = load.resize((250, 250), Image.ANTIALIAS)
            tk.Label(self, text="Распознавания лица для регистрация поциента", font=self.controller.title_font,fg="#263942").place(x=50,y=20)
            render = PhotoImage(file='homepagepic.png', width=750)
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x=470,y=170)
            tk.Label(self, text="Домашная страница", font=self.controller.title_font,fg="#263942").place(x=90,y=150)
            tk.Button(self, text="Добавить пациент", width=30, height=2, fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageOne")).place(x=100,y=230)
            tk.Button(self, text="Проверить пациента", width=30, height=2, fg="#ffffff", bg="#263942",command=lambda: self.controller.show_frame("PageTwo")).place(x=100,y=300)
            tk.Button(self, text="Выход", fg="#263942", width=30, height=2, bg="#ffffff", command=self.on_closing).place(x=100,y=370)

        def on_closing(self):
            if messagebox.askokcancel("Quit", "Are you sure?"):
                global names
                with open("nameslist.txt", "w") as f:
                    for i in names:
                        f.write(i + " ")
                self.controller.destroy()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text="          Информация о пациенте          ", font='Helvetica 25 bold').grid(row=0, column=2,rowspan=2, columnspan=2, pady=10,padx=0)
        tk.Label(self, text="Имя пациента", fg="#263942", font='Helvetica 12 bold').grid(row=7, column=1, pady=10, padx=0)
        tk.Label(self, text="Фамилия пациента", fg="#263942", font='Helvetica 12 bold').grid(row=8, column=1, pady=10, padx=0)
        tk.Label(self, text="Отчество пациента", fg="#263942", font='Helvetica 12 bold').grid(row=9, column=1, pady=10, padx=0)
        tk.Label(self, text="Дата рождения", fg="#263942", font='Helvetica 12 bold').grid(row=10, column=1, pady=10, padx=0)
        tk.Label(self, text="Болезнь пациента", fg="#263942", font='Helvetica 12 bold').grid(row=7, column=3, pady=10, padx=0)
        tk.Label(self, text="E-mail почта", fg="#263942", font='Helvetica 12 bold').grid(row=8, column=3, pady=10, padx=0)
        tk.Label(self, text="Адрес пациента", fg="#263942", font='Helvetica 12 bold').grid(row=9, column=3, pady=10, padx=0)
        tk.Label(self, text="Номер телефон", fg="#263942", font='Helvetica 12 bold').grid(row=10, column=3, pady=10, padx=0)
        
        load = PhotoImage(file='dee.png')
        img = tk.Label(self, image=load)
        img.image = load
        img.grid(row=2, column=1, rowspan=5, columnspan=7, sticky="nsew")

        self.first_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.first_name.grid(row=7, column=2, pady=0, padx=0)
        self.last_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.last_name.grid(row=8, column=2, pady=0, padx=0)
        self.sur_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.sur_name.grid(row=9, column=2, pady=0, padx=0)
        self.data_birth_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.data_birth_name.grid(row=10, column=2, pady=0, padx=0)
        self.disease_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.disease_name.grid(row=7, column=4, pady=0, padx=0)
        self.email_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.email_name.grid(row=8, column=4, pady=0, padx=0)
        self.address_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.address_name.grid(row=9, column=4, pady=0, padx=0)
        self.phone_number_name = tk.Entry(self, borderwidth=3, bg="lightgrey", font='Helvetica 11')
        self.phone_number_name.grid(row=10, column=4, pady=0, padx=0)
        self.buttoncanc = tk.Button(self, text="Назад", width=20, bg="#ffffff", fg="#263942", command=lambda: controller.show_frame("StartPage"))
        self.buttonext = tk.Button(self, text="Далее", width=20, fg="#ffffff", bg="#263942", command=self.start_training)
        self.buttoncanc.grid(row=11, column=2, pady=10, ipadx=5, ipady=4)
        self.buttonext.grid(row=11, column=3, pady=10, ipadx=5, ipady=4)

    def start_training(self):
        global names
        if self.first_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return        
        if self.last_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        if self.sur_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        if self.disease_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        if self.email_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        if self.address_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        if self.phone_number_name.get() == "None":
            messagebox.showerror("Error", "Name cannot be 'None'")
            return
        elif self.first_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif self.last_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif self.sur_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif self.disease_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif self.email_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif self.address_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif self.phone_number_name.get() in names:
            messagebox.showerror("Error", "User already exists!")
            return
        elif len(self.first_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        elif len(self.last_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        elif len(self.sur_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        elif len(self.disease_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        elif len(self.email_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        elif len(self.address_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        elif len(self.phone_number_name.get()) == 0:
            messagebox.showerror("Error", "Name cannot be empty!")
            return

        name = self.first_name.get()
        name = self.last_name.get()
        name = self.sur_name.get()
        name = self.disease_name.get()
        name = self.email_name.get()
        name = self.address_name.get()
        name = self.phone_number_name.get()
        names.add(name)
        self.controller.active_name = name
        self.controller.frames["PageTwo"].refresh_names()
        self.controller.show_frame("PageThree")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global names
        self.controller = controller
        tk.Label(self, text="               Select user", fg="#263942", font='Helvetica 25 bold').grid(row=0, column=0, rowspan=2,columnspan=10, padx=10, pady=10)
        self.buttoncanc = tk.Button(self, text="Cancel", width=20, command=lambda: controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        self.menuvar = tk.StringVar(self)
        self.dropdown = tk.OptionMenu(self, self.menuvar, *names)
        self.dropdown.config(bg="lightgrey", width=60)
        self.dropdown["menu"].config(bg="lightgrey")
        self.buttonext = tk.Button(self, text="Next", width=20, command=self.nextfoo, fg="#ffffff", bg="#263942")
        self.dropdown.grid(row=2, column=2,rowspan=2,columnspan=3, ipadx=8, padx=10, pady=10)
        self.buttoncanc.grid(row=2, ipadx=5, ipady=4, column=6, rowspan=2,columnspan=2, pady=10)
        self.buttonext.grid(row=2, ipadx=5, ipady=4, column=9, rowspan=2,columnspan=2, pady=10)

    def nextfoo(self):
        if self.menuvar.get() == "None":
            messagebox.showerror("ERROR", "Name cannot be 'None'")
            return
        self.controller.active_name = self.menuvar.get()
        self.controller.show_frame("PageFour")

    def refresh_names(self):
        global names
        self.menuvar.set('')
        self.dropdown['menu'].delete(0, 'end')
        for name in names:
            self.dropdown['menu'].add_command(label=name, command=tk._setit(self.menuvar, name))

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.numimglabel = tk.Label(self, text="Number of images captured = 0", font='Helvetica 25 bold', fg="#263942")
        self.numimglabel.grid(row=0, column=4, rowspan=2, columnspan=12, sticky="ew", pady=10)
        self.capturebutton = tk.Button(self, text="Capture Data Set", width=25, fg="#ffffff", bg="#263942", command=self.capimg)
        self.trainbutton = tk.Button(self, text="Train The Model", width=28, fg="#ffffff", bg="#263942",command=self.trainmodel)
        self.capturebutton.grid(row=3, column=3, rowspan=2,columnspan=2, ipadx=5, ipady=4, padx=10, pady=20)
        self.trainbutton.grid(row=3, column=8, rowspan=2,columnspan=2, ipadx=5, ipady=4, padx=10, pady=20)

    def capimg(self):
        self.numimglabel.config(text=str("Captured Images = 0 "))
        messagebox.showinfo("INSTRUCTIONS", "We will Capture 30 pic of your Face.")
        x = start_capture(self.controller.active_name)
        self.controller.num_of_images = x
        self.numimglabel.config(text=str("Number of images captured = "+str(x)))

    def trainmodel(self):
        if self.controller.num_of_images < 20:
            messagebox.showerror("ERROR", "No enough Data, Capture at least 300 images!")
            return
        train_classifer(self.controller.active_name)
        messagebox.showinfo("SUCCESS", "The modele has been successfully trained!")
        self.controller.show_frame("PageFour")


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Face Recognition", font='Helvetica 16 bold')
        label.grid(row=0,column=0, sticky="ew")
        button1 = tk.Button(self, text="Face Recognition", command=self.openwebcam, fg="#ffffff", bg="#263942")
        #button2 = tk.Button(self, text="Emotion Detection", command=self.emot, fg="#ffffff", bg="#263942")
        #button3 = tk.Button(self, text="Gender and Age Prediction", command=self.gender_age_pred, fg="#ffffff", bg="#263942")
        button4 = tk.Button(self, text="Go to Home Page", command=lambda: self.controller.show_frame("StartPage"), bg="#ffffff", fg="#263942")
        button1.grid(row=1,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        #button2.grid(row=1,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        #button3.grid(row=2,column=0, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)
        button4.grid(row=1,column=1, sticky="ew", ipadx=5, ipady=4, padx=10, pady=10)

    def openwebcam(self):
        main_app(self.controller.active_name)

    #def gender_age_pred(self):
        #ageAndgender()
    #def emot(self):
        #emotion()


app = MainUI()
app.iconphoto(False, tk.PhotoImage(file='icon.ico'))
app.mainloop()

