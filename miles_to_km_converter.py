from tkinter import *

FONT = ("Arial", 15, "normal")

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)


km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", font=FONT, command=miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()