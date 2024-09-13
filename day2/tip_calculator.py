print("Welcome to tip calculator!")

total_bill = float(input("What was the total bill? $"))
chosen_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
person_count = int(input("How many people to split the bill? "))

tip = round(((total_bill * chosen_tip/100) / person_count), 2)

print(f"Each person should pay ${tip}")
