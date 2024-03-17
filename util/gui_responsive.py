import tkinter as tk

def format_text(text):
    task_new = "- " + text 
    return task_new

def task_handler(task):
    task_list = []
    task_list = [task] + task_list
    return task_list 

def store_txt(txt, nav):
    if nav == 1:
        with open('task.txt', 'a') as file:
            file.write(format_text(txt))
            file.write('\n')
    if nav == 2:
        with open('task.txt', 'r') as file:
            file_contents = file.read()
            return file_contents
    if nav == 9:
        with open('task.txt', 'w') as file:
            file.write("")

def add_task():
    task = entry_task.get()
    store_txt(task, 1)
    entry_task.delete(0, tk.END)

def view_tasks():
    tasks = store_txt("", 2)
    text_tasks.config(state=tk.NORMAL)
    text_tasks.delete('1.0', tk.END)
    text_tasks.insert(tk.END, tasks)
    text_tasks.config(state=tk.DISABLED)

def delete_tasks():
    store_txt("", 9)

# GUI setup
root = tk.Tk()
root.title("Task Manager")

label_task = tk.Label(root, text="Enter Task:")
label_task.pack()

entry_task = tk.Entry(root, width=30)
entry_task.pack()

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.pack()

button_view = tk.Button(root, text="View Tasks", command=view_tasks)
button_view.pack()

button_delete = tk.Button(root, text="Delete All Tasks", command=delete_tasks)
button_delete.pack()

text_tasks = tk.Text(root, height=10, width=50)
text_tasks.pack()

root.mainloop()