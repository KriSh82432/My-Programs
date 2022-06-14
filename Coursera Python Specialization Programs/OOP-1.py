class PartAnimal:
    x = 2
    def party(stuff):
        stuff.x = stuff.x + 1
        print(stuff.x,'constructed...')

an = PartAnimal()
an.party()
an.party()