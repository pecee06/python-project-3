from tkinter import *
import phonenumbers as pno
from phonenumbers import timezone as tz, geocoder as gc, carrier as cr

root = Tk()

root.title('TrueCaller')

root.wm_iconbitmap('logo.ico')

root.minsize(500,350)
root.maxsize(500,350)

Label(root,
text='TrueCaller',
font=('bold',28),
bg='#0F4D92',
fg='white').pack(side=TOP,pady=20,fill=X)

Label(root,
text='',
font=('bold',28),
bg='#0F4D92').pack(side=BOTTOM,pady=20,fill=X)

F = Frame(root)
F.pack()

Label(F,
text='Name :',
font=('bold',15)).grid(row=1,column=0,pady=5)

Label(F,
text='Contact No :',
font=('bold',15)).grid(row=2,column=0,pady=5)

v1 = StringVar()

v2 = StringVar()
v2.set('+91')

Entry(F,
textvariable=v1).grid(row=1,column=1,pady=5)

Entry(F,
textvariable=v2).grid(row=2,column=1,pady=5)

def t_zone():
    if v2.get() == '':
        pass
    else:
        phone = pno.parse(v2.get())
        tzone = tz.time_zones_for_number(phone)

        win2 = Toplevel(root)
        win2.title('Time Zone')
        win2.wm_iconbitmap('logo.ico')
        win2.grab_set()
        win2.minsize(350,200)
        win2.maxsize(350,200)

        Label(win2,
        text=tzone,
        font=('bold',15)).pack()

def detail():
    if v1.get() == '' or v2.get() == '':
        pass
    else:
        phone = pno.parse(v2.get())
        Carrier = cr.name_for_number(phone,'en')
        Region = gc.description_for_number(phone,'en')

        win3 = Toplevel(root)
        win3.title('Time Zone')
        win3.wm_iconbitmap('logo.ico')
        win3.grab_set()
        win3.minsize(350,200)
        win3.maxsize(350,200)

        Label(win3,
        text=f"-----{v1.get()}'s contact number details-----",
        font=('bold',12)).pack()

        Label(win3,
        text=Carrier,
        font=('bold',15)).pack()

        Label(win3,
        text=Region,
        font=('bold',15)).pack()

        v1.set('')
        v2.set('+91')

Button(F,
text='Time Zone',
font=('bold',12),
command=t_zone).grid(row=3,column=3,pady=5)

Button(F,
text='Details',
font=('bold',12),
command=detail).grid(row=4,column=3,pady=5)

root.mainloop()
