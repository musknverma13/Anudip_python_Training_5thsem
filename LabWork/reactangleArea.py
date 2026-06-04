# write a program to find area and perimeter of recatangle

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
if length < 0 or breadth < 0:
    exit("Length and breadth cannot be negative... exited")   
# calculate area and perimeter  
area = length * breadth
print(f"Area of rectangle is: {area}")
perimeter = 2 * (length + breadth)
print(f"Perimeter of rectangle is: {perimeter}")
