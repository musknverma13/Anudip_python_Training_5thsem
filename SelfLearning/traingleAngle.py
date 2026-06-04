# write a program to check if three angles form a triangle and specify its type
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))
# validate the angles of triangle
if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print("Not a triangle: angles must be greater than 0")
elif angle1 + angle2 + angle3 != 180:
    print("Not a triangle: angles do not sum to 180 degrees")
# if the angles form a triangle, determine its type
else:
    print("The angles form a triangle.")
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Type: Right triangle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Type: Obtuse triangle")
    else:
        print("Type: Acute triangle")
