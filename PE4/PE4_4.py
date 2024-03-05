#empty list called "grades"
grades = []
#adding grades to "grade" one at a time
grades.append(57)
grades.append(79)
grades.append(87)
grades.append(96)
grades.append(81)
print(grades)

average = 0

#calculating average for grades
for x in grades:
    
    average += x

#dividing total by number of grades
average = average / len(grades)
#print average, rounded to 2 decimal places
print(round(average, 2))

#method 1 to remove all failing grades (using for loop)
for x in grades:
    if x < 60:
        grades.remove(x)

#print grades with failing grade removed
print(grades)

#method 2 to remove failing grades (with indexing)
grades = [57, 89, 92, 45, 100]

grades.remove(57)
grades.remove(45)
print(grades)

#i, using sum() and len()
print(round(sum(grades) / len(grades), 3)) 

