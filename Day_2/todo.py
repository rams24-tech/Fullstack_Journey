tasks=[]

def add_task():
    task=input("Enter the task: ")
    tasks.append(task)

def view_tasks():
    for i,work in enumerate(tasks, start=1):
        print(str(i)+". "+work)

opt=0
while opt!=3:
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    opt= int(input("Choose an option: "))  
    if opt== 3:
        print("Good bye")
    elif opt == 1:
        add_task()
    elif opt == 2:
        view_tasks()  
    else :
        print("Invalid Choice") 