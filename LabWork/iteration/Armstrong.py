# Accept a number from the user and determine whether it is an Armstrong number or not.
num = int(input("Enter a number to check: "))
original_num = num
#  Find out how many digits the number has
num_of_digits = len(str(num))
#Create a variable to keep track of our running total sum
sum_of_powers = 0
while num > 0:
   
    digit = num % 10
    sum_of_powers += digit ** num_of_digits
    num = num // 10
#  Check if our calculated sum matches the original number
if original_num == sum_of_powers:
    print(original_num, "is an Armstrong number! 🎉")
else:
    print(original_num, "is NOT an Armstrong number. ❌")
