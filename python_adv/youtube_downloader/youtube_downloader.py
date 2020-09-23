from pytube import YouTube
from tkinter import Button, Entry, Radiobutton, StringVar, Tk, Frame, Label, Toplevel, filedialog
from tkinter import ttk
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
        self.download_link_var = StringVar()
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
            textvariable=self.download_link_var,
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
            r'^https://www\.youtube\.com/.+',
            self.download_link_var.get()
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
        new_window = Toplevel(self.master)
        self.master.withdraw()
        new_window.state('zoomed')
        new_window.grid_rowconfigure(0, weight=0)
        new_window.grid_columnconfigure(0, weight=1)

        SecondApp(
            new_window,
            self.download_link_var.get(),
            self.download_type_var.get(),
            self.save_location_var.get(),
        )


class DownloaderApp(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('YouTube downloader')
        # Full screen
        self.state('zoomed')
        self.grid_rowconfigure(0, weight=2)
        self.grid_columnconfigure(0, weight=1)
        DownloaderView()


class SecondApp:
    def __init__(self,
                 download_window,
                 download_link,
                 download_type,
                 save_location
                 ) -> None:
        self.download_window = download_window
        self.download_link = download_link
        self.download_type = download_type
        self.save_location = save_location

        self._test()

    def _test(self):
        yt = YouTube(self.download_link)
        if self.download_type == '1':
            video_type = yt.streams.filter(only_audio=True).first()
            file_size = video_type.filesize
        elif self.download_type == '2':
            video_type = yt.streams.first()
            file_size = video_type.filesize

        Label(
            self.download_window,
            text='Downloading...',
            font=(FONT, 40)
        ).grid(pady=(100, 0))

        self.progress_label = Label(
            self.download_window,
            text='0',
            fg='red',
            font=(FONT, 40)
        )
        self.progress_label.grid(pady=(50, 0))

        self.progress_bar = ttk.Progressbar(
            self.download_window,
            length=500,
            orient='horizontal',
            mode='indeterminate'
        )
        self.progress_bar.grid(pady=(50, 0))
        self.progress_bar.start()


if __name__ == '__main__':
    app = DownloaderApp()
    app.mainloop()
