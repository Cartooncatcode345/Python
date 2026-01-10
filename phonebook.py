

phonebook = []


def add_contact():
    name = input("Enter Name: ")
    number = input("Enter Number: ")
    phonebook.append([name, number])
    print("Contact added successfully! \n")


def view_contacts():
    if phonebook == []:
        print("Phonebook is empty.\n")
    else:
        print("\n--- Phonebook Contacts ---")
        for i in range(len(phonebook)):
            print(i + 1, ".",phonebook[i][0], "-", phonebook[i][1])
        print()


def edit_contact():
    view_contacts()
    if phonebook != []:
         index = int(input("Enter contact number to edit: ")) - 1
         if index >= 0 and index < len(phonebook):
             phonebook[index][0] = input("enter New Name: ")
             phonebook[index][1] = input("enter New Number: ")
             print("Contact updated successfully!\n")
         else:
            print("Invalid choice!\n")



def delete_contact():
    view_contacts()
    if phonebook != []:
        index = int(input("Enter contact number to delete: ")) - 1
        if index >= 0 and index < len(phonebook):
            phonebook.pop(index)
            print("Contact deleted successfully!\n")
        else:
            print("Invalid Choice!\n")



while True:
    print("📞 PHONEBOOK MENU")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")


    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Existing Phonebook. Goodbye! 👋")
        break
    else:
        print("Invalid Choice!\n")