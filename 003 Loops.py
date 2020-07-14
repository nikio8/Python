import random
import sys
while True:
    print("hello")
    print("What is your name?")
    name = input()
    if name != "Joe":
        #loop unitl user is Joe
        continue
    print("Welcome Back!")
    sys.exit()
numOfGuests=0
print("how many guests?")
numOfGuests=int(input())
if numOfGuests:
    print("you will need "+str(numOfGuests)+" seats")
# range(i,j,k) i-start, j-limit, k-step
for i in range(1,15,2):
    print("Aii captain!"+str(random.randint(1,10)+i))