student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Harmonie": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grade = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grade[student] = "Outstanding"
    elif score >= 81:
        student_grade[student] = "Exceeds Expectation"
    elif score >= 71:
        student_grade[student] = "Accepted"
    else:
        student_grade[student] = "Fail"

print(student_grade)
