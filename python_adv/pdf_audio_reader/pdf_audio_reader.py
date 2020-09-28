from tkinter import *
import os
import PyPDF2
import pyttsx3

# engine_obj = pyttsx3.init()
# engine_obj.setProperty('rate', 200)
# engine_obj.setProperty('voice', 'f1')
# engine_obj.say('hello world')
# engine_obj.runAndWait()

# file_path = os.path.join(os.path.dirname(__file__), './sample.pdf')

# with open(file_path, 'rb') as f:
#     pdf_file_reader = PyPDF2.PdfFileReader(f)

#     extracted_text = ""
#     for page in pdf_file_reader.pages:
#         extracted_text += page.extractText()

#     print(extracted_text)


class AudioReaderAppView(Frame):
    def __init__(self):
        super().__init__()


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
