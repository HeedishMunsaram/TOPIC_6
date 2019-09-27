num1 = input("Enter number: ")
num2 = input("Enter number: ")
operator = input("Enter operator")

if operator == '+':
    def add (num1, num2):
        ans = int(num1) + int(num2)
        return ans

elif operator == '-':
    def sub (num1, num2):
        ans = int(num1) - int(num2)
        return ans

elif operator == '*':
    def mul (num1, num2):
        ans = int(num1) * int(num2)
        return ans

elif operator == '/':
    def div (num1, num2):
        ans = int(num1) / int(num2)
        return ans

ans = add(num1, num2)
ans = sub(num1, num2)
ans = mul(num1, num2)
ans = div(num1, num2)
print(ans)