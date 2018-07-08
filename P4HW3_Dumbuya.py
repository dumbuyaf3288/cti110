# CTI110
# P4HW3
# Fatmata Dumbuya
#07/05/2018

#Enter a nonnegative integer? 4
#The factorial of 4 is 24

factorial = int (input("Enter nonnegative number? "))
n = factorial
count = 1
while n > 0:
    if n <= 0:
        count = count * 1
    else:
        count = count * n
        n = n - 1
       
print(count)
