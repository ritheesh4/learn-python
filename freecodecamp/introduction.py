# Type indentification

# testString = 'hello ritheesh'
# stringToInt = int(testString)
# type(stringToInt)


# Defining a fucntion

# def add_two_numbers(a,b):
#     return a+b
# print(add_two_numbers(2,3))

#While loop
# n=0
# while True:
#     if n==3:
#         break
#     print(n)
#     n=n+1


# for loop
# for i in [2,1,5]:
#     print(i)

#fore loop
# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)


# for n in "banaana":
#     print(n)


# word = "nanana"
# i = word.find("na")
# print(i)


#when should use break in for loop example
# for letter in 'Ritheesh':
#     if letter == 't':
#         break
#     print 'current Letter:', letter

#continue statement
# for letter in 'Python':
#     if letter == 'h':
#         continue
#     print 'Current Letter :',letter

#list 
# bookshelf = []
# bookshelf.append("The Effective Engineer")
# bookshelf.append("The engineering works")
# for values in bookshelf:
#     print(values)

#Dictionary data structure. Colelction of key-value pairs.

# dictionary_example = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3"
# }

# dictionary_example["key4"] = "value4"

# print(dictionary_example['key4'])
# for i in dictionary_example:
#     print(i)





# class Vehicle:
#     def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
#         self.number_of_wheels = number_of_wheels
#         self.type_of_tank = type_of_tank
#         self.seating_capacity = seating_capacity
#         self.maximum_velocity = maximum_velocity

# tesla_model_s = Vehicle(4, 'electric', 5, 250)
# print(tesla_model_s)


# class Vehicle:
#     def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
#         self.number_of_wheels = number_of_wheels
#         self.type_of_tank = type_of_tank
#         self.seating_capacity = seating_capacity
#         self.maximum_velocity = maximum_velocity

#     def number_of_wheels(self):
#         return self.number_of_wheels

#     def set_number_of_wheels(self, number):
#         self.number_of_wheels = number  
# print(number_of_wheels)