# CTI-110
# P2T1-Sales Predtion
# Fatmata Dumbuya
# 13th June, 2018

# Get the total cost of meal.
total_cost = float (input ("enter the total cost of meal: "))

# display the total cost of meal
print("the total_cost is $", format(total_cost, ",.2f"))

# Calculate the total cost of meal
print("the tip is 0.18, the food will  cost" + str(( total_cost * 0.18 )) + "$" )
print("the tax is 0.07, the food will  cost" + str(( total_cost * 0.07 )) + "$" )
