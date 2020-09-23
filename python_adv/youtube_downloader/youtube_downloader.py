from numpy.lib.npyio import save
from pytube import YouTube
from tkinter import Button, Entry, Radiobutton, StringVar, Tk, Frame, Label, Toplevel, filedialog
import os
import re
import threading


FONT = 'Arial'
DOWNLOAD_TYPES = [
    ('Audio MP3', 1),
    ('Video MP4', 2)
]


class DownloaderView(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.link_var = StringVar()
        self.download_type_var = StringVar()
        self.download_type_var.set("1")
        self.save_location_var = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        Label(
            self.master,
            text='YouTube Downloader',
            font=(FONT, 70)
        ).grid(pady=(0, 10))

        self.entry_error_label = Label(
            self.master,
            text='',
            font=(FONT, 20)
        )
        self.entry_error_label.grid(pady=(0, 8))

        # Download link
        Label(
            self.master,
            text='Paste any youtube video link below',
            font=(FONT, 20)
        ).grid(pady=(0, 20))

        Entry(
            self.master,
            width=70,
            textvariable=self.link_var,
            font=(FONT, 20)
        ).grid(pady=(0, 15), ipady=2)

        # Download type
        Label(
            self.master,
            text='Choose download type',
            font=(FONT, 20)
        ).grid()

        for text, value in DOWNLOAD_TYPES:
            Radiobutton(
                self.master,
                text=text,
                font=(FONT, 15),
                variable=self.download_type_var,
                value=value
            ).grid()

        # Directory to save
        Label(
            self.master,
            text='Choose directory',
            font=(FONT, 20)
        ).grid()

        Button(
            self.master,
            text='Directory',
            font=(FONT, 15),
            command=self._ask_dir
        ).grid(pady=10)

        Entry(
            self.master,
            width=70,
            textvariable=self.save_location_var,
            font=(FONT, 20)
        ).grid(pady=(0, 15), ipady=2)

        # Download button
        Button(
            self.master,
            text='Download!',
            width=10,
            font=(FONT, 15),
            command=self._download
        ).grid(pady=10)

    def _ask_dir(self) -> None:
        ret_val = filedialog.askdirectory()
        if ret_val:
            self.save_location_var.set(ret_val)

    def _download(self):
        # Download link valid check
        link_is_valid = re.match(
            '^https://youtube.com/.',
            self.link_var.get()
        )
        if not link_is_valid:
            self.entry_error_label.config(
                text='Invalid youtube link', fg='red'
            )
            return
        else:
            self.entry_error_label.config(
                text='',
                fg='black'
            )

        # Save location valid check
        save_location_is_valid = os.path.isdir(self.save_location_var.get())
        if not save_location_is_valid:
            self.entry_error_label.config(
                text='Invalid save location', fg='red'
            )
            return
        else:
            self.entry_error_label.config(
                text='',
                fg='black'
            )

        # Download
        # self.new_window = Toplevel(self.master)
        # self.master.withdraw()

        # self.app = Download(
        #     self.new_window,
        #     self.link_var.get(),
        #     self.save_location_var.get(),
        #     self.download_type_var.get()
        # )


class DownloaderApp(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('YouTube downloader')
        # Full screen
        self.state('zoomed')
        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(0, weight=1)
        DownloaderView()


if __name__ == '__main__':
    app = DownloaderApp()
    app.mainloop()
