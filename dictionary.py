#empty dictionary
my_dict={}
my_dict1={"name":"Nameer","grade":5,"city":"Dhaka"}
print(my_dict1)
print(len(my_dict1))

print(my_dict1["name"])
print(my_dict1["grade"])
print(my_dict1["city"])
#add item
my_dict1['country']="Bangladesh"
print(my_dict1)
#remove item
my_dict1.pop('city')
print(my_dict1)
#access a prticular item using get()
print(my_dict1.get('country'))
#clear all data
my_dict1.clear()
print(my_dict1)
#loops in dictionaries
my_dict1={"name":"Nameer","grade":5,"city":"Dhaka"}
for i in my_dict1:
    print(i)
