
#formats the text before saving it
def format_text(text):
    task_new = "- " + text 
    return task_new

#storing tasks in a list
def task_handler(task):
    task_list = []
    task_list = [task] + task_list
    return task_list 

def store_txt(txt,nav):
    #this function has two modes, write and append
    if nav==1:
        with open('task.txt' , 'a') as file:
            file.write(format_text(task))
            file.write('\n')
#This checks whether the user wants to read the text file
    if nav==2:
        f = open('task.txt', 'r')
        file_contents = f.read()
        print (file_contents)
    if nav==9:
        with open('task.txt', 'w') as file:
            file.write("")

#user prompt
print("""Please Choose your service
      
      # Press 1: For adding tasks. (add each one per time)

      # Press 2: For viewing your todo list. (New Feature !!)

      # Press 9: For deleting all your tasks.  (NO UNDO)
      
      """)



try:
    # tha navigation toolbox for the user
    navigation = int(input("Enter the chosen service: "))
    while (navigation!=1 and navigation!=9 and navigation!=2):
        navigation = int(input("Enter a suitable number please: "))
    while navigation!=-1 and navigation==1:
            task = input("What do you want to accomplish today? ")
            store_txt(task,1)
            navigation = int(input("Want to add another task? press 1 to continute , -1 to kill: "))
    if navigation==2:
        print("Tasks today: ")
        store_txt("",2)
    if navigation==9:
        store_txt("",9)
except:
    print("""
Hey it looks like there's an error with your input
please make sure you entered a suitable input, and reread the prompt.""")


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/joebum/python-utilities-/to-dolist/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    12.0,
    1440.0,
    485.0,
    fill="#FFCACA",
    outline="")

canvas.create_text(
    28.0,
    253.0,
    anchor="nw",
    text="What do you want to accomplish today?",
    fill="#000000",
    font=("Inter Bold", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1005.0,
    y=618.0,
    width=137.0,
    height=75.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    642.0,
    655.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=291.0,
    y=617.0,
    width=702.0,
    height=74.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=786.0,
    y=754.0,
    width=219.0,
    height=58.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=368.0,
    y=754.0,
    width=332.0,
    height=66.0
)
window.resizable(False, False)
window.mainloop()
