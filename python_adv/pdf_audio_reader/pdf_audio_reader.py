from tkinter import *
from tkinter import filedialog
from threading import Thread
import os
import PyPDF2
import pyttsx3


FONT = 'Arial'


class SpeechThread(Thread):
    def __init__(self, engine: pyttsx3.Engine, text: str):
        super().__init__()

        self.engine = engine
        self.text = text

    def run(self):
        self.engine.say(self.text)
        self.engine.startLoop()

    def stop(self):
        self.engine.endLoop()


class AudioReaderAppView(Frame):
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.engine_thread = None
        self.rate_of_speech = StringVar()
        self.male = IntVar()
        self.female = IntVar()
        self.extracted_text = ""
        self._create_widgets()

    def _create_widgets(self):
        # Top frame
        top_frame = Frame(
            self.master,
            width=500,
            height=200,
            bg='indigo'
        )
        top_frame.pack(side='top', fill='both')

        Label(
            top_frame,
            text='PDF to Audio',
            fg='white',
            bg='indigo',
            font=FONT
        ).pack()

        Label(
            top_frame,
            text='Hear your pdf file',
            fg='white',
            bg='indigo',
            font=FONT
        ).pack()

        # Bottom frame
        bottom_frame = Frame(
            self.master,
            width=500,
            height=450,
            bg='light grey'
        )
        bottom_frame.pack(side='top', fill='y')

        Button(
            bottom_frame,
            text='Select pdf file',
            command=self.extract_text,
            padx='70',
            pady='10',
            fg='white',
            bg='black',
            font=FONT
        ).grid(row=0, pady=20, columnspan=2)

        Label(
            bottom_frame,
            text='Enter rate of speech',
            fg='black',
            bg='light grey',
            font=FONT
        ).grid(row=1, column=0, padx=0, pady=15, sticky=W)

        Entry(
            bottom_frame,
            textvariable=self.rate_of_speech,
        ).grid(row=1, column=1, padx=30, pady=15, sticky=W)

        Label(
            bottom_frame,
            text='Select voice',
            fg='black',
            bg='light grey',
            font=FONT
        ).grid(row=2, column=0, padx=30, pady=15, sticky=W)

        Checkbutton(
            bottom_frame,
            text='Male',
            fg='black',
            bg='light grey',
            variable=self.male,
            onvalue=1,
            offvalue=0
        ).grid(row=2, column=1, padx=30, pady=0, sticky=W)

        Checkbutton(
            bottom_frame,
            text='Female',
            fg='black',
            bg='light grey',
            variable=self.female,
            onvalue=1,
            offvalue=0
        ).grid(row=3, column=1, padx=30, pady=0, sticky=W)

        Button(
            bottom_frame,
            text='Play pdf file',
            command=self.start_speaking,
            fg='white',
            bg='black',
            font=FONT
        ).grid(row=4, column=0, pady=65, sticky=W)

        Button(
            bottom_frame,
            text='Stop playing',
            command=self.stop_speaking,
            fg='white',
            bg='black',
            font=FONT
        ).grid(row=4, column=1, padx=30, pady=65, sticky=W)

    def extract_text(self):
        f = filedialog.askopenfile(
            parent=self.master,
            mode='rb',
            title='Choose a pdf file'
        )
        if f:
            reader = PyPDF2.PdfFileReader(f)
            self.extracted_text = ""
            for page in reader.pages:
                self.extracted_text += page.extractText()
            f.close()

    def start_speaking(self):
        self.engine.setProperty('rate', self.rate_of_speech)
        voices = self.engine.getProperty('voices')
        male_voice = voices[0].id
        female_voice = voices[1].id

        male = self.male.get()
        female = self.female.get()
        if (not male and not female) or (male and female):
            self.engine.setProperty('voice', male_voice)
        elif male:
            self.engine.setProperty('voice', male_voice)
        else:
            self.engine.setProperty('voice', female_voice)

        self.engine_thread = SpeechThread(
            engine=self.engine, text=self.extracted_text
        )
        self.engine_thread.start()

    def stop_speaking(self):
        if self.engine_thread:
            self.engine_thread.stop()
            self.engine_thread.join()


class AudioReaderApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x600')
        self.resizable(0, 0)
        self.configure(background='light grey')
        self.title('PDF Audio Reader')
        AudioReaderAppView()


if __name__ == '__main__':
    app = AudioReaderApp()
    app.mainloop()
