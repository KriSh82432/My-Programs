# Inheritance is the way of adding all the capabilities os a parent class to a child class
class PartyAnimal:
    x = 2
    name = ""
    def __init__(stuff, nam):
        stuff.name = nam
        print(stuff.name,'constructed...')
    def party(self):
        self.x = self.x + 5
        print(self.name,', Count :',self.x)
    def __del__(thing):
        print(thing.name,'destructed at',thing.x)

class CricketScore(PartyAnimal):
    score = 183
    def add(bit):
        bit.score = bit.score + 17
        bit.party()
        print(bit.name,', Score :',bit.score)

class CricketWicket(CricketScore):
    wicket = 33
    def pick(ball):
        ball.wicket = ball.wicket + 2
        ball.add()
        print(ball.name,', Wickets :',ball.wicket)

an = PartyAnimal("Krishna")
an.party()

man = CricketScore("Virat")
man.add()

van = CricketWicket('Steyn')
van.pick()