#P5T1
#CTI 110
#Dumbuya
#07/07/2018

#Miles = Kilometers * 0.6214

Conversion_Factor = 0.6214
def main():
    # Get the distance in kilomters.
    kilometers = float (input('Enter a distance in kilometers? '))

    #Display the distance in kilometers.
    show_miles(kilometers)

def show_miles(km):
    #calculate miles
    miles = km * Conversion_Factor

    #display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

#Call  the main function.
main()
