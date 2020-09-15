from tkinter import *
import smtplib
import re


FONT_TYPE = 'calibri 18 bold'


class EmailSenderView(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.sign_in_email = StringVar()
        self.sign_in_password = StringVar()
        self.sign_in_message_info = StringVar()
        self.receiver_email = StringVar()
        self.subject_var = StringVar()
        self.message_var = StringVar()
        self.mail_composition_info_message = StringVar()
        self._create_widgets()

    def _create_widgets(self):
        self._create_sign_in_frame()
        self._create_mail_composition_frame()
        self.hide_login_label()

    def _create_sign_in_frame(self):
        # Sign in frame
        self.sign_in_frame = Frame(self.master, width=1000, height=1000)

        # Sign in label
        sign_in_label = Label(
            self.sign_in_frame,
            width=25,
            text='Enter your credentials',
            font=FONT_TYPE
        )

        # Email
        sign_in_email_label = Label(self.sign_in_frame, text='Email :')
        sign_in_email_entry = Entry(
            self.sign_in_frame,
            textvariable=self.sign_in_email
        )

        # Password
        sign_in_message_label = Label(self.sign_in_frame, text='Password :')
        sign_in_password_entry = Entry(
            self.sign_in_frame,
            show='*',
            textvariable=self.sign_in_password
        )

        # Sign in button
        sign_in_button = Button(
            self.sign_in_frame,
            text='Sign in',
            width=10,
            bg='black',
            fg='white',
            command=self.sign_in
        )

        # Place widgets
        # Sign in window
        self.sign_in_frame.pack()
        sign_in_label.grid(row=0, columnspan=3, pady=10, padx=10)
        sign_in_email_label.grid(row=1, sticky=E, pady=5, padx=10)
        sign_in_message_label.grid(row=2, sticky=E, pady=5, padx=10)
        sign_in_email_entry.grid(row=1, column=1)
        sign_in_password_entry.grid(row=2, column=1)
        sign_in_button.grid(row=3, columnspan=3, pady=10)

    def _create_mail_composition_frame(self):
        # Mail composition message info frame
        self.message_info_frame = Frame(self.master)

        # Mail composition message label
        self.message_info_label = Label(
            self.message_info_frame,
            width=20,
            bg='cyan',
            fg='red',
            font=FONT_TYPE,
            textvariable=self.sign_in_message_info
        )

        # Sign out button
        self.sign_out_button = Button(
            self.message_info_frame,
            text='Sign out',
            bg='black',
            fg='white',
            command=self.sign_out
        )

        # Mail composition frame
        self.mail_composition_frame = Frame(self.master)

        # Mail composition label
        self.mail_composition_label = Label(
            self.mail_composition_frame,
            width=20,
            text='Compose email',
            font=FONT_TYPE
        )

        # Receiver
        receiver_label = Label(self.mail_composition_frame, text='To :')
        receiver_entry = Entry(
            self.mail_composition_frame,
            textvariable=self.receiver_email
        )

        # Subject
        subject_label = Label(
            self.mail_composition_frame,
            text='Subject :'
        )
        subject_entry = Entry(
            self.mail_composition_frame,
            textvariable=self.subject_var
        )

        # Message
        message_label = Label(
            self.mail_composition_frame,
            text='Message :'
        )
        message_entry = Entry(
            self.mail_composition_frame,
            textvariable=self.message_var
        )

        # Send mail button
        send_mail_button = Button(
            self.mail_composition_frame,
            text='Send mail',
            width=10,
            bg='black',
            fg='white',
            command=self.send_mail
        )

        self.mail_composition_message_label = Label(
            self.mail_composition_frame,
            width=20,
            fg='white',
            bg='black',
            font=FONT_TYPE,
            textvariable=self.mail_composition_info_message
        )

        # Place widgets
        # Mail composition window
        self.message_info_frame.pack(
            side=TOP, expand=NO, fill=NONE
        )
        self.message_info_label.grid(
            row=0, column=0, columnspan=2, pady=5
        )
        self.sign_out_button.grid(
            row=0,
            column=4,
            sticky=E,
            pady=10,
            padx=(5, 0)
        )

        self.mail_composition_frame.pack(side=TOP, expand=NO, fill=NONE)
        self.mail_composition_label.grid(row=0, columnspan=3, pady=10)
        receiver_label.grid(row=1, sticky=E, pady=5)
        receiver_entry.grid(row=1, column=1)
        subject_label.grid(row=2, sticky=E, pady=5)
        subject_entry.grid(row=2, column=1)
        message_label.grid(row=3, sticky=E, pady=5)
        message_entry.grid(row=3, column=1)
        send_mail_button.grid(row=6, columnspan=3, pady=10)
        self.mail_composition_message_label.grid(row=7, columnspan=3, pady=5)

    def sign_in(self):
        if self.credential_is_valid():
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.ehlo()
            self.server.starttls()
            self.server.login(
                self.sign_in_email.get(),
                self.sign_in_password.get()
            )

            self.message_info_frame.pack()
            self.mail_composition_frame.pack()
            self.sign_out_button.grid()
            self.sign_in_message_info.set('Signed In!')
            self.master.after(10, self.master.grid)
            self.sign_in_frame.pack_forget()
            self.master.after(10, self.master.grid)
            self.mail_composition_frame.pack()
            self.mail_composition_message_label.grid_remove()
            self.master.after(10, self.master.grid)

    def hide_login_label(self):
        self.message_info_frame.pack_forget()
        self.mail_composition_frame.pack_forget()
        self.master.after(10, self.master.grid)

    def send_mail(self):
        if self.message_is_valid():
            self.mail_composition_label.grid_remove()
            self.master.after(10, self.master.grid)
            try:
                from_email = self.sign_in_email.get()
                to_email = self.receiver_email.get()
                subject = self.subject_var.get()
                message = self.message_var.get()
                formatted_message = f'From: {from_email} \n'\
                                    f'To: {to_email}\n'\
                                    f'Subject: {subject}\n'\
                                    f'{message}'
                self.server.sendmail(from_email, to_email, formatted_message)

                self.mail_composition_label.grid()
                self.mail_composition_label['text'] = 'Mail sent!'
                self.master.after(10, self.mail_composition_label.grid)
            except Exception as e:
                self.mail_composition_label.grid()
                self.mail_composition_label['text'] = 'Error in sending your email.'
                self.master.after(10, self.mail_composition_label.grid)

    def sign_out(self):
        try:
            self.server.quit()
            self.mail_composition_frame.pack_forget()
            self.message_info_frame.pack()
            self.message_info_label.grid()
            self.sign_in_message_info.set('Signned out successfully.')
            self.sign_out_button.grid_remove()
            self.sign_in_frame.pack()
            self.sign_in_password.set('')
            self.master.after(10, self.master.grid)
        except Exception as e:
            self.sign_in_message_info.set('Error in sign out.')

    def credential_is_valid(self):
        email = self.sign_in_email.get()
        password = self.sign_in_password.get()
        if not email or not password:
            self.message_info_frame.pack()
            self.mail_composition_message_label.grid()
            self.sign_in_message_info.set('Fill all the fields.')
            self.sign_out_button.grid_remove()
            self.master.after(10, self.master.grid)
            return False

        EMAIL_REGEX = re.compile(r'[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$')
        if not EMAIL_REGEX.match(email):
            self.message_info_frame.pack()
            self.mail_composition_message_label.grid()
            self.sign_in_message_info.set(
                'Enter a valid email address.'
            )
            self.sign_out_button.grid_remove()
            self.master.after(10, self.master.grid)
            return False

        return True

    def message_is_valid(self):
        email = self.receiver_email.get()
        subject = self.subject_var.get()
        message = self.message_var.get()

        if not email or not subject or not message:
            self.mail_composition_message_label.grid()
            self.mail_composition_info_message.set('Fill in all the places.')
            self.master.after(10, self.master.grid)
            return False

        EMAIL_REGEX = re.compile(r'[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$')
        if not EMAIL_REGEX.match(email):
            self.mail_composition_message_label.grid()
            self.mail_composition_info_message.set(
                'Enter a valid email address.'
            )
            self.master.after(10, self.master.grid)
            return False

        if len(subject) < 3 or len(message) < 3:
            self.mail_composition_message_label.grid()
            self.mail_composition_info_message.set(
                'Enter a at least 3 characters.'
            )
            self.master.after(10, self.master.grid)
            return False

        return True


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
