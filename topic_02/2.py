# Функції для кожної операції
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

# --- Основна програма ---
print("Простий калькулятор")
print("Операції: +, -, *, /")

operation = input("Введіть операцію: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if operation == '+':
    print("Результат:", add(a, b))
elif operation == '-':
    print("Результат:", subtract(a, b))
elif operation == '*':
    print("Результат:", multiply(a, b))
elif operation == '/':
    print("Результат:", divide(a, b))
else:
    print("Невідома операція!")
