from tkinter import *
from datetime import date

root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')

textbox = Text(bg="#BEBEBE", fg="black")

def calculate_age():
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()

        age = today.year - year
        if (today.month, today.day) < (month, day):
            age -= 1

        message = f"Hello {name}! You are {age} years old."
        textbox.insert(END,message)

        


frame = Frame(master=root, height=200, width=360, bg="#000000")

lbl1 = Label(frame, text = "Full name", bg="#000000",fg="white", width=12)
name_entry = Entry(frame)

lbl2 = Label(frame, text = "Date (DD)", bg="#000000",fg="white", width=12)
day_entry = Entry(frame)

lbl3 = Label(frame, text = "Month (MM)", bg="#000000",fg="white", width=12)
month_entry = Entry(frame)

lbl4 = Label(frame, text = "Year (YYYY)", bg="#000000",fg="white", width=12)
year_entry = Entry(frame)

calc_button = Button(root, text="Calculate Age", command=calculate_age, bg="lightblue", font=("Arial", 12))


frame.pack()
lbl1.pack()
name_entry.pack()
lbl2.pack()
day_entry.pack()
lbl3.pack()
month_entry.pack()
lbl4.pack()
year_entry.pack()
calc_button.pack()
textbox.pack()
root.mainloop()