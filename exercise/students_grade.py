#enter the name
#student_scores = {name,score}
#result → student_grades = {name,grade}
#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

student_scores= {'Ronaldo': 92, 'Rooney': 82, 'Messi': 72, 'Beckham' : 62}

student_grades = {}

for key, value in student_scores.items():
    if value > 90 and value <=100:
        student_grades[key] = "Outstanding"
    elif value > 80 and value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif value > 70 and value <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
