# Calculate electricity bill based on the following slab rates:
# 0-100 units: Rs. 5/unit
# 101-200 units: Rs. 7/unit
# 201-300 units: Rs. 10/unit

# Change this number to test different amounts of electricity used
units_consumed = 250  

# We start our bill amount at 0
total_bill = 0

# Slab 1: First 100 units (0 to 100)
if units_consumed <= 100:
    total_bill = units_consumed * 5

# Slab 2: Between 101 and 200 units
elif units_consumed <= 200:
    # You pay for the first 100 units at Rs. 5, 
    # plus the leftover units at Rs. 7
    total_bill = (100 * 5) + ((units_consumed - 100) * 7)

# Slab 3: Between 201 and 300 units
elif units_consumed <= 300:
    # You pay for the first 100 units at Rs. 5,
    # the next 100 units at Rs. 7,
    # plus the leftover units at Rs. 10
    total_bill = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)

else:
    # If someone uses more than 300 units, we charge the remaining at Rs. 10
    total_bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units_consumed - 300) * 10)

# Print the final result
print("Total Electricity Bill: Rs.", total_bill)
