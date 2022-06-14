class PartyAnimal:
    num = 2
    def __init__(self):
        print('It is constructed...')
    def party(stuff):
        stuff.num = stuff.num + 3
        print('So far',stuff.num)
    def __del__(thing):
        print('It is destructed at',thing.num)

an = PartyAnimal()
an.party()
an.party()
an = 4
print('an :',an)