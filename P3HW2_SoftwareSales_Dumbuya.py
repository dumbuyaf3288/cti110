# CTI-110
# P2T1-Sales Predtion
# Fatmata Dumbuya
# 24th June, 2018


# a simple program using main()
def main():
    retail_price = 99
    quantity = int(input("enter number of software packages purchased?"))
    if quantity <=9:
        discount =0
    elif quantity <=19:
        discount =0.1
    elif quantity <=49:
        discount =0.2
    elif quantity <=99:
        discount =0.3
    else:
        discount =0.4
    discount_amount = float (quantity * retail_price * discount)
    total_amount = float ((quantity * retail_price) - discount)
    print ("discount is ",discount )
    print ("quantity is ",quantity)
    print ("discount amount is ",discount_amount )
    print ("total amount is ", total_amount )
        




main ()





#A software company sells a package that retails for $99. They offer bulk discounts for volume purchases (for example, buying many copies to install in a college classroom).
#The discounts are as follows:
#Quantity 10-19: 	10% discount
#Quantity 20-49:	20% discount
#Quantity 50-99:	30% discount
#Quantity 100+:	40% discount
#Write a program that asks the user to enter the number of packages purchased.
#The program should then display the amount of the discount (if any) and the total purchase cost with the discount applied.
