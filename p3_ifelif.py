# DATE - 18/8/24 , SUNDAY

# Conditional Statements :- if-else , switch cases

  #eg1
a = 8
b = 9
if a>b:
  res = "a = {} is greater than b = {}"
  print(res.format(a,b))
elif a==b:
  print("a & b are equal")
else:
  res = "b = {} is greater than a = {}"
  print(res.format(b,a))

  # ternary operators / conditional expressions
print("a is greater than b") if a>b else print("a & b are equal") if a==b else print("b is greater than a")

  # Calculator - if else
print("Calculator :")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
op = int(input("Enter operation(1-4) : "))
if op==1:
  num1 = int(input("Enter num1 : "))
  num2 = int(input("Enter num2 : "))
  res = num1 + num2
  print("Addition = " , res)
elif op==2:
  num1 = int(input("Enter num1 : "))
  num2 = int(input("Enter num2 : "))
  res = num1 - num2
  print("Subtraction = " , res)
elif op==3:
  num1 = int(input("Enter num1 : "))
  num2 = int(input("Enter num2 : "))
  res = num1 * num2
  print("Multiplication = " , res)
elif op==4:
  num1 = int(input("Enter num1 : "))
  num2 = int(input("Enter num2 : "))
  res = num1 / num2
  print("Division = " , res)
else:
  print("Invalid operation")


    # Calculator - Switch Cases

print("Calculator :")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
op = int(input("Enter operation(1-4) : "))
match op :
    case 1:
        num1 = int(input("Enter num1 : "))
        num2 = int(input("Enter num2 : "))
        res = num1 + num2
        print("Addition = " , res)
    case 2:
        num1 = int(input("Enter num1 : "))
        num2 = int(input("Enter num2 : "))
        res = num1 - num2
        print("Subtraction = " , res)
    case 3:
        num1 = int(input("Enter num1 : "))
        num2 = int(input("Enter num2 : "))
        res = num1 * num2
        print("Multiplication = " , res)
    case 4:
        num1 = int(input("Enter num1 : "))
        num2 = int(input("Enter num2 : "))
        res = num1 / num2
        print("Division = " , res)
    