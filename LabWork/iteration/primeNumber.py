# Accept a number from the user and determine whether it is a prime number or not.
number = int(input('Enter a number: '))
if number>1:
    for i in range(2, number):
        if (number % i) == 0:
            
            print(f"1 {i} {number//i} {number}")
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
