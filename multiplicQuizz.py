import pyinputplus as pyip
import random, time

start = time.time()

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    inpStr = '#%s: %s times %s equals = '%(questionNumber+1,num1,num2)
    #print(inpStr)
    try:
        pyip.inputStr(inpStr, allowRegexes=['^%s$'%(num1 * num2)],
                        blockRegexes=[('.*','Incorrect')],
                        timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
print('Time taken: ', time.time() - start,'sec')


