# write a program for displaying battery charging level
charging_level = int(input("Enter the current battery charging level (0-100): "))
electricity_supply = True
if charging_level < 0:
    exit("Invalid charging level. Charging level cannot be negative.")
    charging_level = 0
    print(charging_level)
    
while(charging_level <= 100):
    if(charging_level):
        print(f"Battery charging level: {charging_level}%")
        charging_level += 20
    else:
        break
# ---------------------------------
    print("Battery fully charged!")
