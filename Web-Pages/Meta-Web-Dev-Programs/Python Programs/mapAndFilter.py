menu = ['espresso', 'mocha', 'latter', 'cappuccino', 'cortado', 'americano']

def findCoffee(coffee):
    if coffee[0] == 'c':
        return coffee

mapCoffee = map(findCoffee, menu)
print(mapCoffee)

for name in mapCoffee:
    print(name)

filterCoffee = filter(findCoffee, menu)
print(filterCoffee)

for name in filterCoffee:
    print(name)