A=(input("Enter numerator: "))
B=(input("Enter denominator: "))
try:
    C=int(A)/int(B)
    print(f"Result:{C}")
              
except ZeroDivisionError: 
        print("Cannot divide by zero.")
        
except ValueError:
        print("Please enter valid numbers.")
else:
     print("Division successful.")
     
              
finally:
    print("Program finished.")

