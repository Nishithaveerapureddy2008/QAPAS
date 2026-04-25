# stage2_quiz_menu.py

while True:
    print("\n1. Register Student")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Dept: ")
        print("Registered:", sid, name, dept)

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice")