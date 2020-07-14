
textFile = open('TextFile.txt')

textFileArray = textFile.read()

print('Here is what is inside:\n')
print(textFileArray)

print("ada"*10)
#  typedPassword = input()

# if typedPassword == secretPassword:
#     print('Access granted')
# elif typedPassword == '12345':
#     print('That password is one that an idiot puts on their luggage.')
#     print('Access denied')
# else:
#     print('Access denied') 

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
 print('Hello, Mary')

if password == 'swordfish':
 print('Access granted.')
else:
 print('Wrong password.')

i=1
while i < 5:
    print(i)
    i+=1
    if i==3:
        print('breaked')
        break
