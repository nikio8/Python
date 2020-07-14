import re

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
#['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

vowelRegex = re.compile(r'[aeiouAEIOU]') # custom class
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

consonantRegex = re.compile(r'[^aeiouAEIOU]') # ^ negatice custom class
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world!'))
# <re.Match object; span=(0, 5), match='Hello'>
print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))

wholeStringIsNum = re.compile(r'^\d+$')

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.'))

robocop = re.compile(r'robocop', re.I)

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.') # substitute

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

