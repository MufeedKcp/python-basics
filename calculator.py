num2 = input("Enter a operator(+ - / *):")

num1 = float(input("Enter a number:"))

num3 = float(input("Enter another number:"))

if num2 == "+":
    print(num1 + num3)
elif num2 == "-":
    print(num1 - num3)
elif num2 == "/":
    print(num1 / num3)
elif num2 == "*":
    print(num1 * num3)
else:
    print(f"{num2} is an invalid operator...!")