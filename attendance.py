names = {}

number = int(input("Enter the number of students: "))

for i in range(0, number):
    n = str(input("Enter student name: "))
    a = str(input("Present/Absent: "))
    names[n] = a

print(names)
