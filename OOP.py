class Parrot:


    species=("bird")
    def __init__(self,age,name):
        self.name=name
        self.age=age

blu=Parrot("Blu",10)
print("Blu is a {}".format(blu.species))
print("Blu is a {} years old".format(blu.age))

