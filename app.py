from tkinter import *
from random import *
import requests
import time

try:

    bg_color = '#3d6466'


    def hacker():
        count = 0
        count_limit = 5
        while count < count_limit:
            count += 1
            letters = "qwertyuiopasdfghjklzxcvbnm1234567890zxcvbnmlkjhgfdsaqwertyuiop0987654321"
            password = "".join(choice(letters) for x in range(randint(5, 7)))

            payload = {
                'username': password,
                'password': password,
                'submit': ''
            }
            try:
                url = name.get()
                run = requests.post(url, data=payload)
                if 'Account successfully created' in run.text:
                    q = Label(box, text=f"{run.status_code} done", bg=bg_color)
                    q.pack()
                else:
                    w = Label(box, text="error. You have a problem with the url or the connection or your payload.\n "
                                        "If the website has more that username and password, change the payload\n")
                    w.pack()
                    break
            except requests.exceptions.MissingSchema:
                y = Label(box, text='url missing. Url must contain http or https. Check your request url and try '
                                    'again', bg=bg_color)
                y.pack()
                break
            except requests.exceptions.ConnectionError:
                z = Label(box, text='connection problem', bg=bg_color)
                z.pack()
                break
            except requests.exceptions.InvalidURL:
                z = Label(box, text='invalid url', bg=bg_color)
                z.pack()
                break
        return


    windows = Tk()
    windows.title("app")
    # windows.eval("tk::PlaceWindow . center")
    box = Frame(width=500, height=500, bg=bg_color)
    box.grid(row=1, column=1)
    box.pack_propagate(False)
    text = Label(box, width="45", bg=bg_color, text="Flood a database with password and username\n".upper())
    text.pack()
    s = Label(box, text="Enter url", bg=bg_color)
    s.pack()
    name = Entry(box, width=50)
    name.pack()
    an = Label(box, text="\n", bg=bg_color)
    an.pack()
    btn = Button(box, command=hacker, text="flood", width=10, height=1)
    btn.pack()
    windows.mainloop()

except NameError as a:
    print(f"connection error {a}")
