a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add = a + b
sub = a - b
mul = a * b
print("Addition =", add)
print("Subtraction =", sub)
print("Multiplication =", mul)
if b != 0:
    div = a / b
    print("Division =", div)
else:
    print("Division by zero is not allowed.")