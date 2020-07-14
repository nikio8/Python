# import math
# find min and max
def high_and_low(arr):
    
    s = arr.split(" ")
    r=[]
    for i in s:
        r.append(int(i))
    #s = s.sort()
    
    return " ".join([str(max(r)), str(min(r))])



def high_and_low2(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low3(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))



print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("140 0 1959 2522 -189 1935 1576 2763 1979 1625 61 389 1566 2122 2469 1065 2827 2695 1309 2167 -181 1116")) # return "2827 -189"