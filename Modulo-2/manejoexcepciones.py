def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except:
    print("Error: Division by zero is not allowed")


def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except Exception as e:
    print("Error: Division by zero is not allowed", e)
    print(e.__class__)


def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "Error: No podemos dividir por cero")