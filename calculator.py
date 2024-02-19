num1 = float(input("Enter First Number: "))
operator = input("Enter The Operator: ")
num2 = float(input("Enter Second Number: "))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "/":
  print(num1 / num2)
elif operator == "*":
  print(num1 * num2)
else:
  print("You entered a wrong operator, Please Try Again")
