#CTI 110
#P5HW1
# Average Test grades
# 07/08/2018

 # Calculate the average   
def cal_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5)/5
    return average
# Determine grade letter

def determine_grade(score):
    # This program takes a number grade and outputs a letter grade.

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    grade = ""

    if score >= A_score:
        grade = "A"
    elif score >= B_score:
        grade = "B"
    elif score >= C_score:
        grade = "C"
    elif score >= D_score:
        grade = "D"
    else:
         grade = "F"
         
    return grade

# main function
def main():
    testscore1 = int(input("Enter test score 1 : "))
    testscore2 = int(input("Enter test score 2 : "))
    testscore3 = int(input("Enter test score 3 : "))
    testscore4 = int(input("Enter test score 4 : "))
    testscore5 = int(input("Enter test score 5 : "))

    print (" Test score Grade ")
    print ("1. ", testscore1, "       ", determine_grade(testscore1))
    print ("2. ", testscore1, "       ", determine_grade(testscore2))
    print ("3. ", testscore1, "       ", determine_grade(testscore3))
    print ("4. ", testscore1, "       ", determine_grade(testscore4))
    print ("5. ", testscore1, "       ", determine_grade(testscore5))
    print ("average : ", cal_average(testscore1, testscore2, testscore3, testscore4, testscore5))
    
main()

    
#Write a program that asks the user to enter five test grades.
#The program should then display a letter grade for each score, and finally the average test score.
#Write the following functions for the program:
#main() – this function will control the main flow of the program.
#It will call the next two functions to do most of the work.
#It should also hold the input() commands to allow the user to type in grades.
#calc_average() – this function should accept five test scores (int or float)
#as arguments, and return the average of the scores.
#(In order to calculate an average, you should take the total of all grades,
#and then divide it by the number of grades.)
#determine_grade() – This function should accept a test score (int or float)
#as an argument and return a letter grade for the score. Use the ten-point
#grading scale you used in a previous assignment (90-100 for A, 80-89 for B
#, and so on).
#The letter grade, a string, should be A, B, C, D, or F.
