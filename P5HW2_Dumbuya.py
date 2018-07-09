#P5HW2
#CTI110
#FatmataDumbuya
#07/08/2018

#Guess Random number

def RandomNumberGame():
    import random
    secretnumber = random.randint(1,100)
    response = "y"
    guess = 0

    while secretnumber != guess:
        guess = int(input('Enter secretnumber: '))
        if guess < secretnumber:
            print('too low, try again')
        elif guess > secretnumber:
            print('too high, try again')
        else:
            print ('congratulation!! you have just won')
            response = input('play again? (y for yes)')
    return response
       
#main function              
def main():
    while RandomNumberGame() == 'y':
        RandomNumberGame()
        
#start program
main()
