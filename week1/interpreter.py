# Math Interpreter

x, y, z = input("Expression: ").split(" ")

if y == "+":
    result = float(x) + float(z)
elif y == "-":
    result = float(x) - float(z)
elif y == "*":
    result = float(x) * float(z)
elif y == "/":
    result = float(x) / float(z)
else:
    result = None

if result is not None:
    print(f"{result:.1f}")
