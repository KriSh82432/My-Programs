# Multiple objects
class PartyAnimal:
    x = 0
    name = ""
    def __init__(stuff, nam):
        stuff.name = nam
        print(stuff.name,'constructed...')
    def party(self):
        self.x = self.x + 5
        print(self.name,', Count :',self.x)
    def __del__(thing):
        print(thing.name,'destructed at',thing.x)

an = PartyAnimal("krishna")
an.party()

man = PartyAnimal("Elan")
man.party()

lan = PartyAnimal("Sidharth")
lan.party()

van = PartyAnimal("Sarwesh")
van.party()

an.party()
lan.party()
man.party()
van.party()