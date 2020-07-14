import re
"""
\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S Any character that is not a space, tab, or newline.
"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex2 = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneNumRegex3 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex4 = re.compile(r'\d{3}-\d{3}-\d{4}')

string1 = 'My number is 415-555-4242.'
string2 = 'My number is 415-555-4242 and 415-555-4299.'

mo = phoneNumRegex.search(string1)
print('Phone number found: ' + mo.group())
mo = phoneNumRegex2.search(string1)
print('Phone number found: ' + mo.group())

mo = phoneNumRegex.search(string2)
print('Phone number found: ' + mo.group())

mo = phoneNumRegex3.search(string2)
print('Phone number found: ' + mo.group(1))

print( phoneNumRegex4.findall(string2) )# find all

mo = phoneNumRegex3.search(string2)
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

heroRegex = re.compile (r'Batman|Tina Fey') # | is OR
batRegex1 = re.compile(r'Bat(man|mobile|copter|bat)') # starting with the same
batRegex2 = re.compile(r'Bat(wo)?man') # optional
batRegex3 = re.compile(r'Bat(wo)*man') # multiple match
batRegex4 = re.compile(r'Bat(wo)+man') # wo not optional (opposite of ? )


mo3 = batRegex3.search('The Adventures of Batwoman')
print(mo3.group())

haRegex = re.compile(r'(Ha){3,5}') # min max matches
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print( mo1.group())
#'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?') #has {}?
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
#'HaHaHa'
