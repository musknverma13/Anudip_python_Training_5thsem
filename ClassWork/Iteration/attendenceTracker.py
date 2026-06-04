# attendence tracker

students = int(input("Enter the number of students: "))
attendance = 0
if students < 0:
    exit("Invalid number of students. Number of students cannot be negative.")
    students = 0
    print(students)
if students > 30:
    exit("Invalid number of students. Number of students cannot exceed 30.")
while(attendance <= 30):
    if(attendance):
        print(f"Number of students present: {attendance}")
        attendance += 1
    else:
        break
