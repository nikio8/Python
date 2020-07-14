# Sandwich Maker
# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
# Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.

import pyinputplus as pyip 

pricelist = {'wheat': 2.0, 'white': 2.0, 'sourdough': 2.5,
            'chicken': 10.0, 'turkey': 9.0, 'ham': 8.0, 'tofu': 7.0,
            'cheese':0.5, 'cheddar':0.5, 'Swiss':0.6, 'mozzarella':0.5,
            'mayo':0.2,
            'mustard':0.2,
            'lettuce':0.5,
            'tomato':0.5
}
sandwitch = []
price = 0.0

bread = pyip.inputMenu(['wheat','white','sourdough'], '%s> '%('bread type: wheat, white, or sourdough'))
sandwitch.append(bread)
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], '%s> '%('protein type: chicken, turkey, ham, or tofu'))
sandwitch.append(protein)
cheese = pyip.inputYesNo('cheese? y/n > ')
if cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], '%s> '%('cheese type: cheddar, Swiss, or mozzarella'))
    sandwitch.append(cheese)
mayo = pyip.inputYesNo('mayo? y/n > ')
if mayo == 'yes':    
    sandwitch.append('mayo')
mustard = pyip.inputYesNo('mustard? y/n > ')
if mustard == 'yes':    
    sandwitch.append('mustard')
lettuce = pyip.inputYesNo('lettuce? y/n > ')
if lettuce == 'yes':    
    sandwitch.append('lettuce')
tomato = pyip.inputYesNo('tomato? y/n > ')
if tomato == 'yes':    
    sandwitch.append('tomato')
noOfSandwiches = pyip.inputInt('no of sandwiches? > ', min=1)



print("Your sandwitch: " + ', '.join(sandwitch))

for k in sandwitch:
    price += pricelist[k] * noOfSandwiches
    print('# ' + k + ' ' + str(pricelist[k]) + ' * ' + str(noOfSandwiches))

print('amount due: ' + str(round(price,2)))