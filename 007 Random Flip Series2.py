import random, copy

# in 100  coin tosses, how many times we get 6 in a row of the same coin side ?
def countSeries():
    # declare vars
    flips=""
    tails6="1"*6 
    heads6="0"*6
    countTails = 0
    countHeads = 0

    # create random coin flip
    for i in range(100):
        flips += str(random.randint(0,1))
    # print(flips)

    # slice string and check for match
    k=0
    flipsTemp = ""
    while k < len(flips)-5:
        flipsTemp = flips[k:k+6]
        if tails6 == flipsTemp:
            countTails +=1
            k+=5 #do we count 00000001 and 00000001 (7 in a row) twice or only once?
        if heads6 == flipsTemp:
            countHeads +=1
            k+=5
        k += 1

    # return sum of coin tosses
    return countTails + countHeads

# test series
howManySeries=0
howManyRounds=10000

for l in range(1,howManyRounds):
    howManySeries += countSeries()

print("how many series in " + str(howManyRounds) + " ? "+ str(howManySeries)) 
print("average per test: " + str (howManySeries/howManyRounds))

