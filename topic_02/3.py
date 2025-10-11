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
print("Калькулятор з використанням match-case")
print("Операції: +, -, *, /")

operation = input("Введіть операцію: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

match operation:
    case '+':
        print("Результат:", add(a, b))
    case '-':
        print("Результат:", subtract(a, b))
    case '*':
        print("Результат:", multiply(a, b))
    case '/':
        print("Результат:", divide(a, b))
    case _:
        print("Невідома операція!")
