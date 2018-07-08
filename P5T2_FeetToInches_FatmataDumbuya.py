# video turtorial about feet to inches
# 07/08/2018
# CTI-110 P5T2_FeetToInches 
# Dumbuya


# for the number of inches per foot
INCHES_PER_FOOT = 12

#mai function
def main():
    # get a number of feet from the user
    feet = int(input('Enter a number of feet? '))

    #Convert that to inches
    print(feet,'equals', feet_to_inches(feet), 'inches.')

#the feet_to_inches function convert feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#call the main function.
main()
