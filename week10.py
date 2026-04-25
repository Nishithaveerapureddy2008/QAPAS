# week10_structured_program.py

students = {}
results = {}

questions = ["Capital of India?", "2+2?"]
answers = ["delhi", "4"]


def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    students[sid] = name
    print("Student added!")


def conduct_quiz():
    score = 0
    for i in range(len(questions)):
        ans = input(questions[i] + ": ").lower()
        if ans == answers[i]:
            score += 1
    return score


def store_result(sid, score):
    results[sid] = score


def show_results():
    print("\nResults:")
    for sid, score in results.items():
        print(sid, ":", score)


def main():
    while True:
        print("\n1.Add Student  2.Quiz  3.Results  4.Exit")
        ch = input("Choice: ")

        if ch == "1":
            add_student()

        elif ch == "2":
            sid = input("Enter ID: ")
            score = conduct_quiz()
            store_result(sid, score)
            print("Score:", score)

        elif ch == "3":
            show_results()

        elif ch == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# Entry point (IMPORTANT for Week 10)
if __name__ == "__main__":
    main()