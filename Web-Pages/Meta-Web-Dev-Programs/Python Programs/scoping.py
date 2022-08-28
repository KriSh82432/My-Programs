def animals():
    animal = "Snake"
    def animal1():
        nonlocal animal
        animal = "Panther"
        print("Inside nested function: "+animal)
    print("Main function: "+animal)
    animal1()
    print("After nested function: "+animal)

animal = "Tiger"
animals()
print("Global: "+animal)