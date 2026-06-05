number=int(input("Enter the number: "))
if number%2==0 and number!=0:
    print(f"{number} is Even")
elif number==0:
    print(f"{number} is zero")     
else:
    print(f"{number} is Odd")  
if number<0:
    print(f"{number} is Negative")
elif number==0:
    print(f"{number} is zero")        
else:
    print(f"{number} is Positive")          