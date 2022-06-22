class Gov:

    grant =25000
    tax = 15.25

    def getData(self):
        print("this is data function")

class State(Gov):

    def covid(self):
        print(self.grant)



s = State()
s.covid()