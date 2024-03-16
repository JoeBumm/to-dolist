#formats the text before saving it
def format_text(text):
    task_new = "- " + text 
    return task_new

#storing tasks in a list
def task_handler(task):
    task_list = []
    task_list = [task] + task_list
    return task_list 

#user prompt
print("""Please Choose your service
      Press 1 for adding todolists, add each one per time
      press 2 for viewing your todo list (coming soon)
      press -1 for ending the process""")

navigation = int(input("Enter the chosen service: "))
while navigation!=-1 and navigation==1:
    task = input("What do you want to accomplish today? ")
    with open('task.txt' , 'w') as file:
        file.write(format_text(task))
    navigation = int(input("Want to add another task? press 1 to continute , -1 to kill "))





