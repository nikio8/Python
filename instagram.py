x=[1,2,0]
y=x.remove(0)
z=print(1,end="")

#print("  x is %s, y is %s, z is %s"%(x,y,z))

if y or z:
    print('1')
else:
    print("2")

raining = False
print("Let's go to the", 'beach' if not raining else 'library')