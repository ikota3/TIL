from tkinter import *
import smtplib
import re


FONT_TYPE = 'calibri 18 bold'


class EmailSenderView(Frame):
    def __init__(self) -> None:
        super().__init__()
        self._create_widgets()

    def _create_widgets(self):
        # LOGIN WINDOW
        self.login_frame = Frame(self.master, width=1000, height=1000)
        self.login_frame.pack()

        self.credentials_label = Label(
            self.login_frame,
            width=25,
            text='Enter your credentials',
            font=FONT_TYPE
        )
        self.credentials_label.grid(row=0, columnspan=3, pady=10, padx=10)

        self.email_label = Label(self.login_frame, text='Email :')
        self.email_entry = Entry(self.login_frame)
        self.password_label = Label(self.login_frame, text='Password :')
        self.password_entry = Entry(self.login_frame, show='*')

        self.email_label.grid(row=1, sticky=E, pady=5, padx=10)
        self.email_entry.grid(row=1, column=1)
        self.password_label.grid(row=2, sticky=E, pady=5, padx=10)
        self.password_entry.grid(row=2, column=1)

        self.login_button = Button(
            self.login_frame,
            text='Login',
            width=10,
            bg='black',
            fg='white',
            command=lambda: login()
        )
        self.login_button.grid(row=3, columnspan=3, pady=10)

        # LOGGED IN WINDOW
        self.logged_in_frame = Frame(self.master)
        self.logged_in_message_frame = Frame(self.logged_in_frame)
        self.logged_in_message_frame.pack(side=TOP, expand=NO, fill=NONE)
        self.login_success_label = Label(
            self.logged_in_message_frame,
            width=20,
            bg='cyan',
            fg='red',
            text='Log in success',
            font=FONT_TYPE)
        self.login_success_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.logout_button = Button(
            self.logged_in_message_frame,
            text='Log out',
            bg='black',
            fg='white',
            command=lambda: logout()
        )
        self.logout_button.grid(
            row=0,
            column=4,
            sticky=E,
            pady=10,
            padx=(5, 0)
        )

        self.logged_in_subject_frame = Frame(self.logged_in_frame)
        self.logged_in_subject_frame.pack(side=TOP, expand=NO, fill=NONE)

        self.label_c = Label(
            self.logged_in_subject_frame,
            width=20,
            text='Compose email',
            font=FONT_TYPE)
        self.label_c.grid(row=0, columnspan=3, pady=10)

        self.to_email_label = Label(self.logged_in_subject_frame, text='To :')
        self.to_email_entry = Entry(self.logged_in_subject_frame)
        self.subject_label = Label(
            self.logged_in_subject_frame,
            text='Subject :')
        self.subject_entry = Entry(self.logged_in_subject_frame)
        self.message_label = Label(
            self.logged_in_subject_frame,
            text='Subject :')
        self.message_entry = Entry(self.logged_in_subject_frame)
        self.to_email_label.grid(row=1, sticky=E, pady=5)
        self.to_email_entry.grid(row=1, column=1)
        self.subject_label.grid(row=2, sticky=E, pady=5)
        self.subject_entry.grid(row=2, column=1)
        self.message_label.grid(row=3, sticky=E, pady=5)
        self.message_entry.grid(row=3, column=1)

        self.send_mail_button = Button(
            self.logged_in_subject_frame,
            text='Send mail',
            width=10,
            bg='black',
            fg='white',
            command=lambda: send_mail()
        )
        self.send_mail_button.grid(row=6, columnspan=3, pady=10)

        self.lab = Label(
            self.logged_in_subject_frame,
            width=20,
            fg='white',
            bg='black',
            font=FONT_TYPE)
        self.lab.grid(row=7, columnspan=3, pady=5)

        self.hide_login_label()

    def login(self):
        if credential_is_valid():
            email = str(self.email_entry.get())
            password = str(self.password_entry.get())
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(email, password)

            self.logged_in_frame.pack()
            self.logout_button.grid()
            self.login_success_label['text'] = 'Logged In!'
            self.master.after(10, self.master.grid)
            self.login_frame.pack_forget()
            self.master.after(10, self.master.grid)
            self.logged_in_subject_frame.pack()
            self.lab.grid_remove()
            self.master.after(10, self.master.grid)

    def hide_login_label(self):
        self.logged_in_frame.pack_forget()
        self.master.after(10, self.master.grid)


class EmailSenderApp(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Email Sender')
        EmailSenderView()


def main():
    app = EmailSenderApp()
    app.mainloop()


if __name__ == '__main__':
    main()
