import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("Python ToDo")

label = tk.Label(root,text="Hello World", font=('Arial', 18))
label.pack(padx=20,pady=20)

textbox = tk.Text(root, height = 3 , font=('Arial', 16))
textbox.pack(padx=10)

# button = tk.Button(root, text="Click me", font=('Arial', 18))
# button.pack(padx=10,pady=10)


# I guess here you are just adding columns like in the calculators
buttom_frame = tk.Frame(root)
buttom_frame.columnconfigure(0, weight=1)
buttom_frame.columnconfigure(1, weight=1)
buttom_frame.columnconfigure(2, weight=1)


btn1 = tk.Button(buttom_frame, text="1", font=('Arial', 18))
# To stretch the whole buttoms accross the window
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttom_frame, text="2", font=('Arial', 18))
# To stretch the whole buttoms accross the window
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttom_frame, text="3", font=('Arial', 18))
# To stretch the whole buttoms accross the window
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttom_frame, text="4", font=('Arial', 18))
# To stretch the whole buttoms accross the window
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttom_frame, text="5", font=('Arial', 18))
# To stretch the whole buttoms accross the window
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttom_frame, text="6", font=('Arial', 18))
# To stretch the whole buttoms accross the window
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttom_frame.pack(fill='x')

## This is an entry place
# myentry = tk.Entry(root)
# myentry.pack()

root.mainloop()