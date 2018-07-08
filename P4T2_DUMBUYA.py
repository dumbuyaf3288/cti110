#CTI 110
#P4T2 DEBUG
#FatmataDumbuya
#07/08/2018

total = 0

# get the bugs collected for each day.
for day in range (1,8):
     print('Enter the bugs collected on day', day)
     bugs = int(input())
     total += bugs
# Display the total bugs.
print ('you have collected a total of ', total)
