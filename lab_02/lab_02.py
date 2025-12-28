import csv
from sys import argv

students = [
    {"name": "Bob", "phone": "0630987654321", "address": "Peremogi 12", "date": "11.06.2013"},
    {"name": "Emma", "phone": "0630987654321", "address": "Peremogi 13", "date": "15.03.2012"},
    {"name": "Jon", "phone": "0630987654321", "address": "Peremogi 14", "date": "26.01.2004"},
    {"name": "Zak", "phone": "0630987654321", "address": "Peremogi 15", "date": "24.07.2005"}
]

def load_CSV():
    if len(argv) < 2:
        print("No CSV file specified. Using default list.")
        return

    file_name = argv[1]

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            students.clear()
            for row in reader:
                students.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "address": row["address"],
                    "date": row["date"]
                })
        print("CSV loaded:", file_name)
    except FileNotFoundError:
        print("CSV file not found. Using default list.")

def save_CSV():
    file_name = "lab2_out.csv"

    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "address", "date"])
        writer.writeheader()
        writer.writerows(students)

    print("CSV saved:", file_name)

def printAllList():
    for elem in students:
         strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Adress is " + elem["address"] + ", Date of birth is " + elem["date"]
         print(strForPrint)
    return

def addStudent():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    date = input("Enter date of birth: ")

    new_item = {"name": name, "phone": phone, "address": address, "date": date}

    pos = 0
    for s in students:
        if name > s["name"]:
            pos += 1
        else:
            break

    students.insert(pos, new_item)
    print("Student added.")

def deleteStudent():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"] == name:
            students.remove(s)
            print("Student deleted.")
            return

    print("Student not found.")

def updateStudent():
    name = input("Enter name to update: ")

    for s in students:
        if s["name"] == name:
            students.remove(s)
            break
    else:
        print("Student not found.")
        return

    new_name = input("New name: ")
    new_phone = input("New phone: ")
    new_address = input("New address: ")
    new_date = input("New date: ")

    new_item = {"name": new_name, "phone": new_phone, "address": new_address, "date": new_date}

    pos = 0
    for s in students:
        if new_name > s["name"]:
            pos += 1
        else:
            break

    students.insert(pos, new_item)
    print("Student updated.")

def main():
    load_CSV()

    while True:
        action = input("\nChoose action [C-create, U-update, D-delete, P-print, X-exit]: ")

        match action:
            case "C" | "c":
                addStudent()
                printAllList()
            case "U" | "u":
                updateStudent()
                printAllList()
            case "D" | "d":
                deleteStudent()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                save_CSV()
                print("Exit.")
                break
            case _:
                print("Invalid option.")

main()
