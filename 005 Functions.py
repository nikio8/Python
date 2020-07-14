import sys, time

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
    return "a"
    #sys.exit()

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

def frst(s):
    return "A"+str(s)

print(a())
print(frst("dam"))


try:
    goRight=True
    goLeft=False
    i=0

    while True:
        if goRight:
                if i == 10:
                    goRight = False
                else:
                    i += 1
        else:
            if i == 0:
                    goRight=True
            else:
                i -= 1
        print(" "*i,end="")
        print("*"*10)
        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()