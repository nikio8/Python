import pyinputplus as pyip

# for i in range(2):
#  response = pyip.inputNum('Enter a number: ')

# response = pyip.inputNum('>', min=4, lessThan=6)
# response = pyip.inputNum(blank=True)
# #help(pyip.inputChoice)
# response = pyip.inputNum(limit=2)
# response = pyip.inputNum(timeout=10)
response = pyip.inputNum("> ", limit=2, default='N/A')
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers) # Return an int form of numbers.

response = pyip.inputCustom(addsUpToTen) # No parentheses after
