class CSStudent:

    #Class Variales
    stream = 'cse'
    #the init method or constructer
    def __init__(self,roll):
        #Instance variables
        self.roll = roll

    def setAddress(self, address):
        self.address = address

#Retrieves Instance variables
    def getAddress(self):
        return self.address
    
# Driver Code
add = CSStudent(101)
add.setAddress("Dhaka, Bangladesh")
print(add.getAddress())