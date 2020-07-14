def likes(names):
    n = len(names)
    print([min(4,n)])
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)



print(likes([])) # // must be "no one likes this"
print(likes(["Peter"]))# // must be "Peter likes this"
print(likes(["Jacob", "Alex"]))# // must be "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))# // must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))# // must be "Alex, Jacob and 2 others like this"