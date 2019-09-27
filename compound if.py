name = input("Enter name: ")
age = int(input("Enter age: "))

if name.isalnum() and not(name.isdigit()):
    print(name + " - You are", age, "years old.")
else:
    print("Please enter a valid name.")