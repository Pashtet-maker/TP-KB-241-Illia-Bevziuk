def discriminant(a, b, c):
    """
    Обчислює дискримінант квадратного рівняння ax^2 + bx + c = 0
    """
    return b**2 - 4*a*c

print(discriminant(1, -3, 2))
print(discriminant(1, 2, 1))
print(discriminant(1, 1, 1))