# write a program to calculate area and perimeter of triangle
# input of three sides
# sides are taken in integer form becoz we can not have a triangle with sides in float form
s1 = int(input("Enter the first side: " ))
s2 = int(input("Enter the second side: " ))
s3 = int(input("Enter the third side: " ))
print("---------------------------------")

# calculate the perimeter
perimeter = s1 + s2 + s3

# calculate the area using heron's formula
s = (s1 + s2 + s3) / 2

area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5



# print the area and perimeter
# print("Area of the triangle is: {:.2f} ".format(area))

print(f"Area of the triangle is: {area:.3f} sq.cm")
print("---------------------------------")
print(f"Perimeter of the triangle is: {perimeter:.2f} cm")
