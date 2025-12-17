list = [
    {"name": "Bob", "phone": "0667834567", "address": "Victory St., 54a", "date": "12.11.2014"},
    {"name": "Emma", "phone": "0638888888", "address": "Wall St., 19", "date": "9.09.2004"},
    {"name": "Jon", "phone": "0635578455", "address": "Broadway St., 34d", "date": "14.04.2005"},
    {"name": "Zak", "phone": "0633345000", "address": "Greenwich St., 55c", "date": "03.08.2011"}
]


def printAllList():
    for elem in list:
         strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Adress is " + elem["address"] + ", Date of birth is " + elem["date"]
         print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    address = input("Please enter student address: ")
    date = input("Please enter student date of birth: ")
    newItem = {"name": name, "phone": phone, "address": address, "date": date}

    insertPosition = 0
    for elem in list:
        if name > elem["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1

    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            break
    if updatePosition == -1:
        print("Student not found")
        return

    new_name = input("New name: ")
    new_phone = input("New phone: ")
    new_address = input("New address: ")
    new_date = input("New date of birth: ")

    del list[updatePosition]
    newS = {"name": new_name, "phone": new_phone, "address": new_address, "date": new_date}

    insertPosition = 0
    for item in list:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newS)
    print("Student updated successfully")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")


main()
