text= input("Enter the text: ")
text=text.lower()
backward_text= text[::-1]
print(backward_text)
if text==backward_text:
    print("Palindrome")
else:
    print("Not a Palindrome")    