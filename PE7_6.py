import random
grades = []
for x in range(1,11):
    grades.append(random.randint(0,100))

passing_grade = int(input("Enter a passing Grade: "))

passing_grades = []
for x in grades:
    if x > passing_grade:
        passing_grades.append(x)
print("Passing Grades: " + str(passing_grades))
print("Original Grades: " + str(grades))