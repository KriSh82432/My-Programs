class myClass:
    x = 5 + 1
    print("Hello there")
    def hello(self, name):
        print("Hello"+" "+name)
        return "How are you?"
    def sum(self, num1, num2):
        return num1+num2

class House:
    totalRooms = 7
    bedRooms = 2
    bathRooms = 2
    kitchen = 1
    commonHall = 1
    prayerHall = 1
    def rooms(self):
        return self.totalRooms


myc = myClass()
print(myc.x)
print(myc.hello("Krishna"))
print(myc.sum(3, 5))

house = House()
print(house.bathRooms)
print(house.bedRooms)

house.bedRooms = 3
print(house.bedRooms)
print(House.bedRooms)

House.bedRooms = 2
print(house.bedRooms)
print(House.bedRooms)

print(house.rooms())