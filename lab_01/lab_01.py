# ===============================================
# Лабораторна робота №1
# ===============================================


students = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@gmail.com",  "group": "TP"},
    {"name": "Emma", "phone": "0637654321", "email": "emma@gmail.com", "group": "KB"},
    {"name": "Jon",  "phone": "0635555555", "email": "jon@gmail.com",  "group": "BI"},
    {"name": "Zak",  "phone": "0639999999", "email": "zak@gmail.com",  "group": "TK"},
]



def printAllList():
    print("\n=== Список студентів ===")
    for elem in students:
        print(
            f"Name: {elem['name']}, "
            f"Phone: {elem['phone']}, "
            f"Email: {elem['email']}, "
            f"Group: {elem['group']}"
        )
    print("========================\n")
    return


# -------------------------------------------------
# Функція для додавання нового студента
# -------------------------------------------------
def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть email: ")
    group = input("Введіть групу: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    # Знаходить позицію для вставки (щоб список залишався відсортованим)
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, newItem)
    print("Новий елемент було додано!\n")
    return


# -------------------------------------------------
# Функція для видалення існуючого запису
# -------------------------------------------------
def deleteElement():
    name = input("Введіть ім'я студента, якого потрібно видалити: ")
    deletePosition = -1

    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break

    if deletePosition == -1:
        print("Студента не знайдено!\n")
    else:
        del students[deletePosition]
        print("Студента видалено!\n")

    return


# -------------------------------------------------
# Функція для оновлення інформації про студента
# -------------------------------------------------
def updateElement():
    name = input("Введіть ім'я студента, якого потрібно оновити: ")
    found = False

    for item in students:
        if name == item["name"]:
            found = True
            print(f"Поточні дані: {item}")

            new_name = input(f"Нове ім'я (Enter — залишити '{item['name']}'): ") or item["name"]
            new_phone = input(f"Новий телефон (Enter — залишити '{item['phone']}'): ") or item["phone"]
            new_email = input(f"Новий email (Enter — залишити '{item['email']}'): ") or item["email"]
            new_group = input(f"Нова група (Enter — залишити '{item['group']}'): ") or item["group"]

            # Оновлюємо дані
            item["name"] = new_name
            item["phone"] = new_phone
            item["email"] = new_email
            item["group"] = new_group

            
            students.sort(key=lambda x: x["name"])

            print("Дані студента оновлено!\n")
            break

    if not found:
        print("Студента не знайдено!\n")

    return


# -------------------------------------------------
# Основне меню програми
# -------------------------------------------------
def main():
    while True:
        choice = input(
            "Оберіть дію:\n"
            "[C] — створити\n"
            "[U] — оновити\n"
            "[D] — видалити\n"
            "[P] — показати всіх\n"
            "[X] — вихід\n"
            "Ваш вибір: "
        ).strip().lower()

        if choice in ("c", "create"):
            print("\nДодавання нового студента:")
            addNewElement()
            printAllList()

        elif choice in ("u", "update"):
            print("\nОновлення даних студента:")
            updateElement()
            printAllList()

        elif choice in ("d", "delete"):
            print("\nВидалення студента:")
            deleteElement()
            printAllList()

        elif choice in ("p", "print"):
            printAllList()

        elif choice in ("x", "exit"):
            print("Вихід із програми...")
            break

        else:
            print("Невірний вибір, спробуйте ще раз!\n")


# -------------------------------------------------
# Точка входу
# -------------------------------------------------
if __name__ == "__main__":
    main()