with open("note.txt", "a") as file:
    file.write(input("Enter a note:")+"\n")
    print("Note Saved!")
with open("note.txt", "r") as file:
    text=file.read()
    print("All notes:")
    print(text)
