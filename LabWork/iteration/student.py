# Step 1: Accept marks for 5 subjects from the user
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate the Total Marks
total_marks = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate the Percentage
percentage = (total_marks / 500) * 100

# Determine the Grade using if-elif-else conditions
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print("\n--- YOUR REPORT CARD ---")
print("Total Marks Obtained:", total_marks, "out of 500")
print("Percentage:", percentage, "%")
print("Final Grade:", grade)
