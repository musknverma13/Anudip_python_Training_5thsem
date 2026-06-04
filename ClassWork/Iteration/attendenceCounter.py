#  a teacher is taking attendence . strength of class is 30 . every time he needs to insert whether student is present or absent . count the total number of student present as well as absent

students = int(input("Enter the number of students: "))
present_count = 0
absent_count = 0
attendance = 0

while attendance < students:
    attendance += 1
    status = input(f"Student {attendance}: Enter 'P' for present or 'A' for absent: ").strip().upper()

    if status == 'P' or status == 'PRESENT':
        present_count += 1
    elif status == 'A' or status == 'ABSENT':
        absent_count += 1
    else:
        print("Invalid input. Please enter 'P' for present or 'A' for absent.")
        attendance -= 1
        continue

print("\nAttendance Summary")
print(f"Total students: {students}")
print(f"Present: {present_count}")
print(f"Absent: {absent_count}")
