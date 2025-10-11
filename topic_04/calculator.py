# --- Функции арифметических операций ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Обработка исключения деления на ноль
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
        return None


# --- Функция безопасного ввода чисел ---
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")


# --- Основная программа ---
def calculator():
    print("=== Калькулятор с обработкой исключений ===")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'exit'\n")

    while True:
        try:
            op = input("Выберите операцию (+, -, *, /): ").strip()

            if op.lower() == 'exit':
                print("Завершение работы программы.")
                break

            if op not in ['+', '-', '*', '/']:
                raise ValueError("Неизвестная операция!")

            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)

            if result is not None:
                print(f"Результат: {result}\n")

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


# --- Запуск программы ---
if __name__ == "__main__":
    calculator()
