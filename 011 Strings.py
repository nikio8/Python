""" this chapter
discusses
strings"""

''' 
isalpha() Returns True if the string consists only of letters and isn’t blank
isalnum() Returns True if the string consists only of letters and numbers and is not blank
isdecimal() Returns True if the string consists only of numeric characters and is not blank
isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

startswith() and endswith()
'''

name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))

name2="Kiki"
age2=90
print(f'My name is {name2}. and I am {age2 + 1} years old next year.')


print(ord('a'))
print(chr(35))