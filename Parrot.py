class Parrot:


    species=("bird")
    def __init__(self,age,name):
        self.name=name
        self.age=age
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self):
        return "{} now dancing",format(self.name)        

blu=Parrot("Blu",10)
print(blu.sing("Happy"))
print(blu.dance())
print("Blu is a {}".format(blu.species))
print("Blu is a {} years old".format(blu.age))
