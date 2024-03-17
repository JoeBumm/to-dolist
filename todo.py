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


