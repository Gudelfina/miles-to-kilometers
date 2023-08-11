from tkinter import *


def miles_to_kilometers():
    miles_input = float(entry.get())
    result = round(miles_input * 1.609)
    conversion.config(text=result)


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=2, row=1)

miles = Label(text="Miles ")
miles.grid(column=3, row=1)

equal_to_label = Label(text="is equal to ")
equal_to_label.grid(column=1, row=2)

conversion = Label(text="0 ")
conversion.grid(column=2, row=2)

kilometers = Label(text="Km")
kilometers.grid(column=3, row=2)

button = Button(text="Calculate", command=miles_to_kilometers)
button.grid(column=2, row=3)


window.mainloop()
