class recipes():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The " + self.dish + " contains " + str(self.items) + \
            " and takes " + str(self.time) +" to prepare")
        
pizza = recipes("Pizza", ["Cheese", "Bread", "Tomato"], 45)
pasta = recipes("Pasta", ["Penne", "Sauce"], 60)

pizza.contents()
pasta.contents()