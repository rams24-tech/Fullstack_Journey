def intro():
    print("HII , This is Kasi Rama Rao")
    print("I am pursuing mu Masters in computer science at University of Texas at Arlington")
    print("I will be graduating by may 2026 withg a cgpa of 3.65")
intro()    
intro()

def table(x):
    for i in range(1,11):
        print(x*i)
table(3)        
table(5)
table(7)

def add(A,B):
    return (A+B)

sum1=add(10,5)
print(sum1)
print(add(add(1,2), add(3,4)))