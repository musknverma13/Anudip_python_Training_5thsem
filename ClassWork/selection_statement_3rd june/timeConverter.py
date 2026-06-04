# program to convert time in corresponding hour, minute and second
# input time in second
second = int(input("Enter time in seconds: "))
# check second is negative or not
if second < 0:
    exit("Time cannot be negative... exited")
    hour = minute = 0
if(second >= 3600):
# calculate hour, minute and second
    hour = second // 3600
    second = second % 3600
if second>=60:
    minute = second  // 60      
    second = second % 60
# print time in hour, minute and second
    print(f"Time is {hour} hour, {minute} minute and {second} second")
