try:
    number=int(input("Enter a number: "))
    print(number*number)
except ValueError:
    print("Please enter a valid Number!")
