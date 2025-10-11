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

print("Калькулятор. Введіть 'exit' щоб завершити.\n")

while True:
    operation = input("Операція (+, -, *, /) або 'exit': ").strip()

    if operation.lower() == 'exit':
        print("Програма завершена.")
        break

    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: потрібно вводити числа!")
        continue

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

    print("-" * 40)