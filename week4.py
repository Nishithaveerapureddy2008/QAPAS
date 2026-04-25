# stage4_modular_quiz.py

questions = ["Capital of India?", "2+2?"]
answers = ["delhi", "4"]

def display_questions():
    for i, q in enumerate(questions):
        print(i+1, q)

def accept_answers():
    user_ans = []
    for q in questions:
        user_ans.append(input(q + ": ").lower())
    return user_ans

def evaluate(user_ans):
    score = 0
    for i in range(len(answers)):
        if user_ans[i] == answers[i]:
            score += 1
    return score

display_questions()
ua = accept_answers()
print("Score:", evaluate(ua))