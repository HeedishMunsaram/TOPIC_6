age = int(input("Enter age: "))
name = input("Enter name: ")

if age > 65 or age < 18:
    print("Congrats you meet the age requirements" , name + ".")
else:
    print("You are not in the required age ranges", name + ".")