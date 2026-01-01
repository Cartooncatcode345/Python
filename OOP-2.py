#Creating the robot with a class
class Robot:
    def __init__(self, name):
        self.name = name


    def introduce(self):
        print("Hello! I am ", self.name)


robot1 = Robot("Robo")
robot2 = Robot("Techy")



robot1.introduce()
robot2.introduce()