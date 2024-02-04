
# class Person:
#    def __init__(self, name, age): #double underscore for init. use this to assign variables to class
#      self.names = name #assign a variable (using 1st parameter.variablename) to the other parameters in the init fucntion
#      self.ages = age
# person1 = Person("kenny", 23) #new object created- assigns variable to name/age parameter in Person class

# print(person1.names) #use obj name + variable name without 1st parameter to access the class parameters
# print(person1.ages)
# print(person1.names) #use obj name + variable name without 1st parameter to access the class parameters
# print(person1.ages)

# '''to control what should be returned when class object is represented as a string
# use _str_() function'''

# print(person1) #printing person1 object without variable name will describe person as an object only

# class Person2:
#   def __init__(self, name, age):
#     self.names = name
#     self.ages = age

#   def __str__(self): 
#     return f"{self.names}({self.ages})" #this will allow the values to be printed when obj is called without variables

# person2 = Person2("kenny", 23)
# print(person2) #values of object variables will be printed even though obj is without variable name
# '''Objects can be functions- 
# functions that belong to objects are object methods'''
class Person3:
    def __init__(me):
        me.names = None #can assign variable as none if u don't have parameter
        me.ages = None
    def myfunc(you): #function that is executed on the person3 object. 1st parameter of obj function must be used to access variable in class
      b = you.ages
      a = print('hi my name is ' , you.names) 
      return b    
    def aaa(self):
       self.ages = 23
       #return self.myfunc()
      
person3 = Person3()
person3.names = 'kenny' #assigns the name variable to this value kenny
person3.myfunc()
person3.aaa()