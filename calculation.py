# The function now handles all 7 Python arithmetic operators
def pro(N, A, B):
    if N == "ADD":
        return A + B
    elif N == "SUB":
        return A - B
    elif N == "MUL":
        return A * B
    elif N == "DIV":
        if B == 0:
            return "Error: Cannot divide by zero!"
        return A / B
    elif N == "MOD":
        return A % B   # Remainder
    elif N == "POW":
        return A ** B  # Power/Exponent
    elif N == "FLOOR":
        if B == 0:
            return "Error: Cannot divide by zero!"
        return A // B  # Division without decimals
    else:
        return "Invalid Operation!"

# This part runs the calculator and asks for user input
print("--- Advanced Python Calculator ---")
print(""" Options: ADD, SUB, MUL, DIV ,
MOD (Remainder), POW (Power), FLOOR (Whole Number Div)""")

op = input("Enter operation: ").upper()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = pro(op, num1, num2)

print("---------------------------")
print(f"Result: {result}")
print("---------------------------")
