import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image
import smtplib
from email.message import EmailMessage
import sqlite3  # for storing emails and passwords data
import webbrowser  # to open app password
import os

# Customtkinter customizations
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


class SignUpPage(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title('Signup ')
        self.geometry('800x500')
        self.resizable(False, False)

        self.main_frame = CTkFrame(self,
                                   width=700,
                                   height=400,
                                   corner_radius=20)
        self.main_frame.grid(row=1, column=1, sticky='nsew')

        # Defining grids
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=10)
        self.main_frame.columnconfigure(2, weight=40)
        self.main_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

        # ----------------------------- Main page ----------------------------------
        # First name fields
        self.first_name_lab = CTkLabel(self.main_frame,
                                       text='First name:',
                                       font=('Verdana', 15))
        self.first_name_lab.grid(row=0, column=0)

        self.first_name_entry = CTkEntry(self.main_frame,
                                         width=300,
                                         placeholder_text='Enter your first name')
        self.first_name_entry.grid(row=0, column=1, sticky='W', padx=30)

        # Last name fields
        self.last_name_lab = CTkLabel(self.main_frame,
                                      text='Last name:',
                                      font=('Verdana', 15))
        self.last_name_lab.grid(row=1, column=0)

        self.last_name_entry = CTkEntry(self.main_frame,
                                        width=300,
                                        placeholder_text='Enter your last name')
        self.last_name_entry.grid(row=1, column=1, sticky='W', padx=30)

        # Email fields
        self.email_lab = CTkLabel(self.main_frame,
                                  text='Email:',
                                  font=('Verdana', 15))
        self.email_lab.grid(row=2, column=0)

        self.email_entry = CTkEntry(self.main_frame,
                                    width=300,
                                    placeholder_text='Enter your email')
        self.email_entry.grid(row=2, column=1, sticky='W', padx=30)

        # Password fields
        self.password_lab = CTkLabel(self.main_frame,
                                     text='Google App Password:',
                                     font=('Verdana', 15, 'underline'),
                                     text_color='#5DADE2')
        self.password_lab.grid(row=3, column=0)

        self.password_entry = CTkEntry(self.main_frame,
                                       width=300,
                                       placeholder_text='Enter your password',
                                       show='*')
        self.password_entry.grid(row=3, column=1, sticky='W', padx=30)

        self.check_var = IntVar(value=0)
        self.checkbox = CTkCheckBox(self.main_frame,
                                    text="Show Password",
                                    variable=self.check_var,
                                    onvalue="1",
                                    offvalue="0",
                                    command=self.show_password)
        self.checkbox.grid(row=3, column=2, ipadx=10)

        # Signup button
        self.signup_btn = CTkButton(self.main_frame,
                                    text='Signup',
                                    corner_radius=20,
                                    command=self.storing_data)
        self.signup_btn.grid(row=4, column=0, ipadx=5)

        # Bindings
        self.password_lab.bind("<Button-1>", lambda e: self.open_app_pass())


    def open_app_pass(self):
        webbrowser.open_new_tab('https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4NdRcPRt1ImCOMdmu8Fip8ir6C4O_nMXGHRZtxR1ESGz1ZuJzBR' )

    def show_password(self):

        if self.check_var.get() == 1:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')

    def storing_data(self):
        """
        Stores value first and last name, email and google app password
        :param self:
        :return:
        """
        f_name = self.first_name_entry.get()
        l_name = self.last_name_entry.get()
        email_addr = str(self.email_entry.get())
        app_pass = self.password_entry.get()

        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        try:
            c.execute("""CREATE TABLE user_data (
                        first_name text,
                        last_name text,
                        email text,
                        app_pass text)""")
        except sqlite3.OperationalError:
            print('')


        if f_name and l_name and email_addr and app_pass != None: # if the fields are filled then
            c.execute(f"SELECT * FROM user_data WHERE email='{email_addr}'")
            value = c.fetchone() # all the values from the database

            # User_info is to store the data of the user in a tuple
            user_info = ()
            info = list(user_info)

            info.append(str(f_name))
            info.append(str(l_name))
            info.append(str(email_addr))
            info.append(str(app_pass))

            user_info = tuple(info)
            print(user_info, end='\n\n')
            print(value)

            if value != None and value == user_info: # If in the database and matches with user_info then show error message
                messagebox.showerror('Database Error', "This is already in the database so can't be added again.")

            elif value != None and value != user_info:  # If in the database and doesn't match with user_info then show error message
                messagebox.showerror('Database Error', "This data cannot be added to the database because the email already exist in our database and can't have another profile of the same email.")

            elif value == None: # if not in the database then insert in the database and show message that it is inserted
                c.execute(f"INSERT INTO user_data VALUES ('{f_name}', '{l_name}', '{email_addr}', '{app_pass}')") # insert the data in the database
                messagebox.showinfo('Information added', 'Your information has been inserted into the database')

        else:
            messagebox.showerror('Information missing', "You haven't entered your information yet. Please enter your information.")

        conn.commit()
        conn.close()


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
                                   height=200,
                                   corner_radius=15)
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
                                       hover_color='#1A9FD5',
                                       )
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
                                         placeholder_text='Enter your email address', )
        self.email_addr_entry.grid(row=0, column=1, sticky='W')

        self.check_button = CTkButton(self.main_frame,
                                      text='Check Password',
                                      width=100,
                                      command=self.check_password)
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

    def add_account_page(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SignUpPage()  # create window if its None or destroyed
        else:
            self.toplevel_window.deiconify()  # if window exists focus it

    def check_password(self):
        global password
        password = None
        sender_email = self.email_addr_entry.get().lower()

        conn = sqlite3.connect('data.db')
        c = conn.cursor()

        try:
            c.execute(f"SELECT * FROM user_data WHERE email='{sender_email}'")
            password_fetch = c.fetchone() # this is a tuple with the information
            password = password_fetch[3]
            print(password_fetch, password)

            messagebox.showinfo("Verified", 'Your password is verified')
        except:
            messagebox.showinfo("Data Error", "Your data is not recorded in our database. Please sign in and try again")

    def send_mail(self):
        try:
            sender_addr = self.email_addr_entry.get().lower()
            receiver_addr = self.to_addr_entry.get().lower()
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

            messagebox.showinfo('Mail Sent', f'Your email was successfully sent to {receiver_addr}')

        except:
            messagebox.showerror('Password error', 'Please press on the check button to send email.')



app = App()
app.mainloop()
