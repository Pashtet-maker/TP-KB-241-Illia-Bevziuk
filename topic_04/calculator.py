def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка ділення на 0 неможливе!")
        return None


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка введіть коректне число!")



def calculator():
    print("=== Калькулятор з обробкою вийнятків ===")
    print("Доступні операції: +, -, *, /")
    print("Для вихіда натисніть 'exit'\n")

    while True:
        try:
            op = input("Виберіть операцію (+, -, *, /): ").strip()

            if op.lower() == 'exit':
                print("Завершення роботи програми.")
                break

            if op not in ['+', '-', '*', '/']:
                raise ValueError("Невідома операція!")

            a = get_number("Введіть перше число: ")
            b = get_number("Введіть друге число: ")

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
            print(f"Невідома помилка: {e}")
            
            if name == "__main__":
    calculator()


if __name__ == "__main__":
    calculator()
