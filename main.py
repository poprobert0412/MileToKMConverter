from tkinter import *

windows = Tk()
windows.title("Mile To KM Converter")
windows.minsize(300, 200)

def calculate_to_km():
    miles = float(input.get())
    km_value = round(miles * 1.6, 2)
    km.config(text=km_value)


my_label = Label(text="Miles", font=("Arial", 15, "bold"))
my_label.pack()
my_label.place(x=190, y=50)

equal = Label(text="is equal to", font=("Arial", 12, "bold"))
equal.pack()
equal.place(x=40, y=100)

km = Label(text=0, font=("Arial", 12, "bold"))
km.pack()
km.place(x=130, y=100)

button = Button(text="Calculate", command=calculate_to_km)
button.pack()
button.place(x=150, y=140)


input = Entry(width=10)
input.pack()
input.place(x=110, y=55)



km_show = Label(text="KM", font=("Arial", 12, "bold"))
km_show.pack()
km_show.place(x=190, y=100)





windows.mainloop()