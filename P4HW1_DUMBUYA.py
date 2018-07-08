#P4HW1
#CTI110
#Fatmata Dumbuya
#07/05/2018

speed = int(input("what is the speed of the vechicle in mph:"))
hours = int(input("how many hours has it travelled:"))
count = 0
print ("Hours Distance travelled")
print ("........................")
while count < hours:
    count = count + 1
    print("  ", count,  "  " ,speed * count )
    
#print ("distance:", (speed * hour))
