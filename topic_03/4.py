def find_insert_position(sorted_list, value):
    """Повертає позицію (індекс), куди слід вставити value, щоб зберегти порядок."""
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            return i
    return len(sorted_list)  # вставити в кінець, якщо елемент найбільший

# --- Тест ---
nums = [1, 3, 5, 7, 9]
print("Відсортований список:", nums)

new_val = float(input("Введіть нове число для вставки: "))
pos = find_insert_position(nums, new_val)

print(f"Позиція для вставки: {pos}")

# Показати, як буде виглядати список після вставки
nums.insert(pos, new_val)
print("Новий список:", nums)
