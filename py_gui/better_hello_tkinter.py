import tkinter as tk
from tkinter import ttk


class HelloView(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.name = tk.StringVar()
        self.hello_message = tk.StringVar()
        self.hello_message.set("Hello World!")
        self.create_widgets()

    def create_widgets(self):
        name_label = ttk.Label(self, text="Name: ")
        name_entry = ttk.Entry(self, textvariable=self.name)
        ch_button = ttk.Button(self, text='Change', command=self.on_change)
        hello_label = ttk.Label(self, textvariable=self.hello_message, font=(
            'TkDefaultFont', 64), wraplength=600)

        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=tk.W+tk.E)
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.hello_message.set(f'Hello {self.name.get()}')
        else:
            self.hello_message.set('Hello')


class HelloApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title('Hello Tkinter')
        self.geometry('800x600')
        self.resizable(0, 0)
        HelloView(self).grid(sticky=tk.NSEW)
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = HelloApplication()
    app.mainloop()
