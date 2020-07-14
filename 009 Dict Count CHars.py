import pprint
message = ' It was a bright cold day in April, and the clocks were striking thirteen.'.strip()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print('Item: '+k+' '+str(v).rjust(18-len(k)))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)




