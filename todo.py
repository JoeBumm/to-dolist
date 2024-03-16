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
      Press 1 for adding todolists, add each one per time
      press 2 for viewing your todo list (coming soon)
      press -1 for ending the process
      For deleting all your tasks, press 9 (no undo !!)""")

# tha navigation toolbox for the user
navigation = int(input("Enter the chosen service: "))


while navigation!=-1 and navigation==1:
    task = input("What do you want to accomplish today? ")
    store_txt(task,1)
    navigation = int(input("Want to add another task? press 1 to continute , -1 to kill "))
if navigation==2:
    print("Tasks today: ")
    store_txt("",2)
if navigation==9:
    store_txt("",9)

