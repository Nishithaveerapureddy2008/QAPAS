# week9_modular_style.py

# -------- STUDENT MODULE --------
students = {}

def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    students[sid] = name
    print("Student added!")

def view_students():
    print("\nStudents:")
    for sid, name in students.items():
        print(sid, ":", name)


# -------- QUIZ MODULE --------
questions = ["Capital of India?", "2+2?"]
answers = ["delhi", "4"]

def conduct_quiz():
    score = 0
    for i in range(len(questions)):
        ans = input(questions[i] + ": ").lower()
        if ans == answers[i]:
            score += 1
    print("Score:", score)
    return score


# -------- RESULT MODULE --------
results = {}

def store_result(sid, score):
    results[sid] = score

def show_results():
    print("\nResults:")
    for sid, score in results.items():
        print(sid, ":", score)


# -------- MAIN LOGIC --------
while True:
    print("\n1.Add Student  2.Quiz  3.Results  4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()

    elif ch == "2":
        sid = input("Enter ID: ")
        score = conduct_quiz()
        store_result(sid, score)

    elif ch == "3":
        show_results()

    elif ch == "4":
        break

    else:
        print("Invalid choice")