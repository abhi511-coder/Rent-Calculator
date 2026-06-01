## Inputs we need from user 
# total rent
# total food ordered for snacking 
# Electricity units spend
# Charge per unit

## Output
# Total amount you have to pay is


rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity units spent = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in a room = "))

total_bill = electricity_spend * charge_per_unit

total_expense = rent + food + total_bill

per_person = total_expense / persons

print("Total expense =", total_expense)
print("Each person will pay =", per_person)