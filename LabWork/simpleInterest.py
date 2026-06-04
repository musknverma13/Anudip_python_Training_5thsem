# write a program to calculate simple interest
# input principal, rate and time
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
if principal < 0 or rate < 0 or time < 0:
    exit("Principal, rate and time cannot be negative... exited")
# calculate simple interest
simple_interest = (principal * rate * time) / 100
# print simple interest
print(f"Simple interest is: {simple_interest}")

