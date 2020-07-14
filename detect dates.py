import re

testRegex = re.compile(r'r+\w{1,}')
isDateRegex = re.compile(r'''(
    \s(\d)?\d             # day
     (/|-|\.)+                  # separator
    (\d)?\d                # month
    (/|-|\.)                   # separator
    \d{4}               # last 4 digits
    )''', re.VERBOSE)


text0 = ' dater r rested'
text1 = ' date is  12/02/1999 rested'
text2 = ' date is 12.02.1999 rested'
text3 = ' date is 12-02-1999 rested'
text4 = ' date is 1/02/1999 rested' #not
text5 = ' date is 02/2/1999 rested'

text6 = ' date is 122/1999 rested'
text7 = ' date is 50/2/1999 rested'
text8 = ' date is 01/2/9999 rested'

# print(testRegex.findall(text0))
# print(isDateRegex.findall(text1))
# print(isDateRegex.findall(text2))
# print(isDateRegex.findall(text3))
# print(isDateRegex.findall(text4))
# print(isDateRegex.findall(text5))
# print('__space__')
# print(isDateRegex.findall(text6))
# print(isDateRegex.findall(text7))
# print(isDateRegex.findall(text8))

text = str(text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8)
print(text)
print(isDateRegex.findall(text))

matches = []
for groups in isDateRegex.findall(text):
    dates = '-'.join([groups[0]])
    # print(dates)
    # if groups[0] != '':
    #     dates += ' x' + groups[0]
    matches.append(dates.strip().replace('-','/').replace('.','/'))

# TODO: Copy results to the clipboard.
if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No dates found.')
    