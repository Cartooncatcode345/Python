

slam_book = []   


def add_entry():
    print("\n--- Add Slam Entry ---")
    name = input("Friend's Name: ")
    nickname = input("Nickname: ")
    color = input("Favourite Color: ")
    hobby = input("Hobby: ")
    dream = input("Dream: ")

    slam_book.append([name, nickname, color, hobby, dream])
    print("Slam entry added successfully!\n")


def view_entries():
    if slam_book == []:
        print("\nNo slam entries yet.\n")
    else:
        print("\n--- Slam Book Entries ---")
        for i in range(len(slam_book)):
            print("\nEntry", i + 1)
            print("Name        :", slam_book[i][0])
            print("Nickname    :", slam_book[i][1])
            print("Fav Color   :", slam_book[i][2])
            print("Hobby       :", slam_book[i][3])
            print("Dream       :", slam_book[i][4])
        print()


while True:
    print("📘 SLAM BOOK MENU")
    print("1. Add Slam Entry")
    print("2. View Slam Book")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("Thank you for using Slam Book! 😊")
        break
    else:
        print("Invalid option. Try again!\n")
