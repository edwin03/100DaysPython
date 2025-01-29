student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for name in student_scores:
    sScore = student_scores[name]
    if sScore >= 91:
        student_grades[name] = "Outstanding"
    elif sScore >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif sScore >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)