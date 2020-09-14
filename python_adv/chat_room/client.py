import tkinter
import socket
from tkinter import *
from threading import Thread

FONT_NAME = 'Arial'
HOST = 'localhost'
PORT = 8080


class ChatRoomView(Frame):
    def __init__(self) -> None:
        super().__init__()
        self.msg = StringVar()
        self._create_widgets()
        self._create_socket()

    def _create_widgets(self) -> None:
        msg_frame = Frame(self.master, height=100, width=100, bg='#204051')
        msg_frame.pack()

        scroll_bar = Scrollbar(msg_frame)
        self.msg_list = Listbox(
            msg_frame,
            height=15,
            width=100,
            bg='#3b6978',
            yscrollcommand=scroll_bar.set
        )
        scroll_bar.pack(side=RIGHT, fill=Y)
        self.msg_list.pack(side=LEFT, fill=BOTH)

        label = Label(
            self.master,
            text='Enter the message',
            fg='#e4e3e3',
            font=FONT_NAME,
            bg='#84a9ac'
        )
        label.pack()

        entry_field = Entry(
            self.master,
            textvariable=self.msg,
            fg='#3b6978',
            width=50
        )
        entry_field.pack()

        send_button = Button(
            self.master,
            text='Send',
            font=FONT_NAME,
            fg='#84a9ac',
            command=self._send
        )
        send_button.pack()

        quit_button = Button(
            self.master,
            text='Quit',
            font=FONT_NAME,
            fg='#84a9ac',
            command=self._on_closing
        )
        quit_button.pack()

    def _send(self) -> None:
        msg = bytes(self.msg.get(), 'utf8')
        self.sock.send(msg)
        self.msg.set("")
        if msg == '#quit':
            self.sock.close()
            self.receive_thread.join()
            self.master.destroy()

    def _on_closing(self) -> None:
        self.msg.set('#quit')
        self._send()

    def _create_socket(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        self.receive_thread = Thread(target=self._receive)
        self.receive_thread.start()

    def _receive(self) -> None:
        while True:
            try:
                msg = self.sock.recv(1024).decode('utf8')
            except BaseException:
                print('There is an error receiving the message.')
            else:
                self.msg_list.insert(tkinter.END, msg)


class ChatRoomApplication(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Chat Room App')
        self.configure(bg='#204051')
        ChatRoomView().pack()


def main() -> None:
    app = ChatRoomApplication()
    app.mainloop()


if __name__ == '__main__':
    main()
