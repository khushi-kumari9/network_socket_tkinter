import socket
import threading
from tkinter import *

def handle_receive(listbox):
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            listbox.insert(END, "server: " + msg)
        except:
            break

def send(listbox, entry):
    msg = entry.get()
    listbox.insert(END, "client: " + msg)
    s.send(msg.encode("utf-8"))
    entry.delete(0, END)

# GUI Setup
root = Tk()
root.title("Client")
listbox = Listbox(root, height=15, width=50)
listbox.pack()
entry = Entry(root, width=40)
entry.pack(side=LEFT)
button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=LEFT)

# Socket Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 12345))

# Thread to receive messages
threading.Thread(target=handle_receive, args=(listbox,), daemon=True).start()

root.mainloop()
