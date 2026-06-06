tasks=[]
def add_task(task):
    tasks.append(task)

def view_tasks():
    n=1
    for i in tasks:
        print(str(n)+". "+i)
        n=n+1

    
add_task("Buy Milk")
add_task("Finish Assignment")
add_task("Call Mom")

view_tasks()