# write a program to check the three side form a triangle or not
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
# validate the sides of triangle
if side1 < 0 or side2 < 0 or side3 < 0:
    exit("Side cannot be negative... exited")
print("--------------------------------")
print(f"Sides of triangle are: {side1}, {side2} and {side3}")
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print("The sides form a triangle")
else:
    print("The sides do not form a triangle")
