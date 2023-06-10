a = int(input("Enter number of students N: "))

names = []
for j in range(a):
    names.append(input("Enter student name: "))

marks = []
for i in range(a):
    marks.append(input("Enter marks of students in first subject:"))
    marks.append(input("Enter marks of students in second subject:"))
    marks.append(input("Enter marks of students in third subject:"))
    marks.append(input("Enter marks of students in fourth subject:"))
    marks.append(input("Enter marks of students in fifth subject:"))

for a, b in zip(names, marks):
    print(a+" - "+b)