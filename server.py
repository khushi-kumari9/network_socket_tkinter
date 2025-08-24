import socket
import threading
from tkinter import *

def handle_receive(listbox):
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            listbox.insert(END, "client: " + msg)
        except:
            break

def send(listbox, entry):
    msg = entry.get()
    listbox.insert(END, "server: " + msg)
    client.send(msg.encode("utf-8"))
    entry.delete(0, END)

# GUI Setup
root = Tk()
root.title("Server")
listbox = Listbox(root, height=15, width=50)
listbox.pack()
entry = Entry(root, width=40)
entry.pack(side=LEFT)
button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=LEFT)

# Socket Setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 12345))
server.listen(1)
listbox.insert(END, "Waiting for client to connect...")
client, _ = server.accept()
listbox.insert(END, "Client connected successfully.")


# Thread to receive messages
threading.Thread(target=handle_receive, args=(listbox,), daemon=True).start()

root.mainloop()
