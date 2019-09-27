name = input("Enter name: ")
age = int(input("Enter age: "))

if age < 18:
    print(name + " You are", age, "years old my child")
elif age > 18 and age < 30:
    print(name + " You are", age, "years old young adult")
elif age > 30 and age < 50:
    print(name + " You are", age, "years old. This is middle age.")
elif age > 50:
    print(name + " You are", age, "years old and very wise.")