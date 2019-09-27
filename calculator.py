num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
operator = input("What is your operation? Enter + - * or / only: ")

if operator == "+":
    answer = (num1+num2)
elif operator == "-":
    answer = (num1-num2)
elif operator == "*":
    answer = (num1*num2)
elif operator == "/":
    answer = (num1/num2)

else:
    print("This is not a valid operation!")
print(str(answer))