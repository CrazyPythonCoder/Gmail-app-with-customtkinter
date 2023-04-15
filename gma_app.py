import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import messagebox
from PIL import Image

import smtplib
from email.message import EmailMessage


# Customtkinter customizations
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


class SignUpPage(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title('Signup ')
        self.geometry('800x500')

        # Defining grids
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)

        self.main_frame = CTkFrame(self, width=700, height=400)
        self.main_frame.grid(row=1, column=1, sticky='nsew')

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.rowconfigure(0, weight=1)

        self.username_label = CTkLabel(self.main_frame, text='Username')
        self.username_label.grid(row=0, column=0)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Configurations
        self.title('Gmail Sender')
        self.geometry('1200x750')

        self.attachment_file_img = CTkImage(light_image=Image.open('file.png'))

        # ------------------------ ---------- Defining frames -----------------------------------------
        self.top_frame = CTkFrame(self,
                                  width=1000)
        self.top_frame.grid(row=0, column=0, sticky='new')

        self.main_frame = CTkFrame(self,
                                   width=1000,
                                   height=200)
        self.main_frame.grid(row=1, column=0, sticky='nsew', pady=30, padx=40)

        # ----------------------------------- Defining grids -----------------------------------------
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=30)
        # self.columnconfigure(1, weight=1)

        self.top_frame.rowconfigure((0, 1, 2), weight=1)
        self.top_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        self.main_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        # self.main_frame.rowconfigure(4, weight=3)
        self.main_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.main_frame.columnconfigure(5, weight=10)

        # ----------------------------------- Navbar -----------------------------------------------

        self.top_frame_lab = CTkLabel(self.top_frame,
                                      text='Gmail Sender',
                                      font=('Ubuntu', 20))
        self.top_frame_lab.grid(row=1, column=0, sticky='W', pady=25, padx=20)

        # self.login_button = CTkButton(self.top_frame,
        #                               text='Login',
        #                               command=self.login_page_appear,
        #                               width=100)
        # self.login_button.grid(row=1, column=7, sticky='E', padx=0)

        self.signup_button = CTkButton(self.top_frame,
                                       text='Add Account',
                                       width=100,
                                       command=self.add_account_page,
                                       fg_color='#01B6FF',
                                       hover_color='#1A9FD5')
        self.signup_button.grid(row=1, column=8)

        self.toplevel_window = None

        # ---------------------------------- The main area --------------------------------

        # From ---------------------------
        self.email_addr_lab = CTkLabel(self.main_frame,
                                       text='Email Address:',
                                       text_color='white',
                                       font=('Verdana', 15))
        self.email_addr_lab.grid(row=0, column=0, sticky='W', padx=20)

        self.email_addr_entry = CTkEntry(self.main_frame,
                                         width=350,
                                         placeholder_text='Enter your email address',)
        self.email_addr_entry.grid(row=0, column=1, sticky='W')

        self.check_button = CTkButton(self.main_frame,
                                      text='Check',
                                      width=100)
        self.check_button.grid(row=0, column=1, sticky='E')

        # To ---------------------------------------------------

        self.to_addr_lab = CTkLabel(self.main_frame,
                                    text='To:',
                                    text_color='white',
                                    font=('Verdana', 15))
        self.to_addr_lab.grid(row=1, column=0, sticky='W', padx=20)

        self.to_addr_entry = CTkEntry(self.main_frame,
                                      width=350,
                                      placeholder_text='Enter the email address you want to send the email to')
        self.to_addr_entry.grid(row=1, column=1, sticky='W')

        # Subject -------------------------------------------------

        self.subject_lab = CTkLabel(self.main_frame,
                                    text='Subject:',
                                    text_color='white',
                                    font=('Verdana', 15))
        self.subject_lab.grid(row=2, column=0, sticky='W', padx=20)

        self.subject_entry = CTkEntry(self.main_frame,
                                      width=350,
                                      placeholder_text='Enter your subject')
        self.subject_entry.grid(row=2, column=1, sticky='W')

        # Message ---------------------------------------------------------
        self.message_lab = CTkLabel(self.main_frame,
                                    text='Message:',
                                    text_color='white',
                                    font=('Verdana', 15))
        self.message_lab.grid(row=3, column=0, sticky='NW', padx=20)

        self.message_entry = CTkTextbox(self.main_frame,
                                        width=500,
                                        border_width=1)
        self.message_entry.grid(row=3, column=1, sticky='nsew')

        # Send button and attachment button ------------------------------------------------------
        self.send_button = CTkButton(self.main_frame,
                                     width=120,
                                     text='Send Mail',
                                     corner_radius=20,
                                     command=self.send_mail)
        self.send_button.grid(row=4, column=0)

        self.attach_button = CTkButton(self.main_frame,
                                       width=1,
                                       image=self.attachment_file_img,
                                       text='',
                                       corner_radius=50,
                                       fg_color='#2b2b2b',
                                       hover_color='#403D3D')
        self.attach_button.grid(row=4, column=1, sticky='W')

    def add_account_page(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SignUpPage()  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def send_mail(self):
        sender_addr = self.email_addr_entry.get()
        password = 'ayyvhlokzsrqnqam'
        receiver_addr = self.to_addr_entry.get()
        subject = self.subject_entry.get()
        mail_msg = self.message_entry.get(1.0, END)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_addr
        msg['To'] = receiver_addr
        msg.set_content(mail_msg)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_addr, password)
            smtp.send_message(msg)


app = App()
app.mainloop()
