# stage5_result_storage.py

results = {}  # {student_id: score}
student_ids = set()
attempts = []

sid = input("Enter ID: ")
score = int(input("Enter score: "))

if sid not in student_ids:
    student_ids.add(sid)
    results[sid] = score
    attempts.append((sid, score))
else:
    print("Duplicate student!")

print(results)
print(attempts)