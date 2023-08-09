'''
# Singleton Borg pattern
#Singleton behavior can be implemented by Borg’s pattern but instead of having only one instance of the class, 
#there are multiple instances that share the same state. Here we don’t focus on the sharing of the instance identity instead we focus on the sharing state
'''
class Monostate:
 
    # state shared by each instance
    __shared_state = dict()
 
    # constructor method
    def __init__(self):
 
        self.__dict__ = self.__shared_state  # The __dict__ in Python represents a dictionary or any mapping object that is used to store the attributes of the object.
        self.state = 'Sleeping'
 
    def __str__(self):
 
        return self.state
 
 
# main method
if __name__ == "__main__":
 
    mono1 = Monostate()    # object of class Monostate
    mono2 = Monostate()    # object of class Monostate
    mono3 = Monostate()    # object of class Monostate
 
    mono1.state = 'Running'  # mono1 changed the state
    mono2.state = 'Eating'     # mono2 changed the state
 
    print(mono1)    # output --> Eating
    print(mono2)    # output --> Eating
 
    mono3.state = 'Walking'  # person3 changed the
    # the shared state
 
    print(mono1)    # output --> Walking
    print(mono2)    # output --> Walking
    print(mono3)    # output --> Walking