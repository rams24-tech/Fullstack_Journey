number=int(input("Enter the number:"))
value=1
if number==0:
    print("1")
else:
    while number>1:
        value=value*(number)
        number= number-1    
print(value)