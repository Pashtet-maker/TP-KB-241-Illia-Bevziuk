import math

# Функція розрахунку дискримінанта
def discriminant(a, b, c):
    return b**2 - 4*a*c

# Функція пошуку коренів квадратного рівняння
def find_roots(a, b, c):
    d = discriminant(a, b, c)
    print(f"Дискримінант D = {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Два різних корені: x₁ = {x1}, x₂ = {x2}")
    elif d == 0:
        x = -b / (2*a)
        print(f"Один корінь: x = {x}")
    else:
        print("Коренів немає (дискримінант < 0)")

# --- Основна програма ---
print("Пошук коренів квадратного рівняння ax² + bx + c = 0")
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

find_roots(a, b, c)