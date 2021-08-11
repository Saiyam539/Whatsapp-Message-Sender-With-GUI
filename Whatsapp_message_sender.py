from tkinter import *
import pywhatkit

def send_msg():
    number = int(phone_number.get())
    Message = message.get("1.0",END)
    timing = time.get()
    timing2 = timing.split(":")
    hour = int(timing2[0])
    print(hour)
    min = int(timing2[1])
    print(hour)
    pywhatkit.sendwhatmsg(f"+91{number}",Message,hour,min,3,browser=None)


window = Tk()
window.maxsize(600,650)
window.minsize(600,650)
window.title("Whatsapp Message Sender")
window.config(bg="light blue")

heading = Label(window,text="Whatsapp Message Sender",font=("bold",50),bg="light green")
heading.pack(fill=X)

label_1 = Label(window,text="Phone Number:",font=("bold",30),bg="light blue")
label_1.place(x=20,y=100)
phone_number = Entry(window,font=("bold",30),width=15)
phone_number.place(x=250,y=100)

label_2 = Label(window,text="Message:",font=("bold",30),bg="light blue")
label_2.place(x=20,y=170)
message = Text(window,font=("bold",25),width=18,height=5)
message.place(x=250,y=170)

Lable_3 = Label(window,text="Time(Ex-17:09): ",font=("bold",25),bg="light blue")
Lable_3.place(x=20,y=350)
time = Entry(window,font=("bold",30),width=15)
time.place(x=250,y=350)

button = Button(window,text="Send Message",font=("bold",30),command=lambda:send_msg())
button.place(x=200,y=550)

window.mainloop()