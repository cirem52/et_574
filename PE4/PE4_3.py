#creating a list with courses I am taking
courses = ["ET574", "PH111", "CALC-I", "ENG-LITERATURE", "ENG131"]
#set x to equal to the amount of items in the list "courses"
x = len(courses)
print(f"I am taking {x} courses")

#first and last elements of the list
print(courses[0], courses[-1])

#first four elements of the list
print(courses[0:4])

#last 4 classes
print(courses[1:5])

#all classes except first and last

print(courses[1:-1])
