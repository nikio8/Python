# clipboard program
# use short keyword to fill email

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'test': "Simple text"}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Nothing as an argument to copy. use say ...mclip.py busy ')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

# to run the program
# enter py filepath\mclip.py TEXT
# if found it will copy text to clipboard

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase.upper() + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)