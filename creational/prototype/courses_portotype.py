'''
Prototype pattern

#declare a common interface or class which supports object cloning which allows us to clone the object without coupling our code to the class of that method. 
#An object that supports cloning is called as Prototype.

Advantages:
#Less number of SubClasses : All the other Creational Design Patterns provides a lot of new subClasses which are definitely not easy to handle 
when we are working on a large project. But using Prototype Design Pattern, we get rid of this.
#Provides varying values to new objects: All the highly dynamic systems allows you to define new behavior through object composition by specifying 
values for an object’s variables and not by defining new classes.
#Provides varying structure to new objects: Generally all the applications build objects from parts and subparts. For convenience, such applications 
often allows you instantiate complex, user-defined structures to use a specific subcircuit again and again

Disadvantages:
#Abstraction: It helps in achieving the abstraction by hiding the concrete implementation details of the class.
#Waste of resources at lower level: It might be proved as the overkill of resources for a project that uses very few objects
'''

from abc import ABC, abstractmethod
import copy


# class - Courses 
class Courses(ABC):
    
    # constructor
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)

# class - DSA course
class DSA(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"

    def course(self):
        print("Inside DSA::course() method")

# class - SDE Course
class SDE(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"

    def course(self):
        print("Inside SDE::course() method.")

# class - STL Course
class STL(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"

    def course(self):
        print("Inside STL::course() method.")

# class - Courses At GeeksforGeeks Cache
class Courses_Cache:
    
    # cache to store useful information
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = Courses_Cache.cache.get(sid, None)
        return COURSE.clone()

    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("sde")
        Courses_Cache.cache[sde.get_id()] = sde

        dsa = DSA()
        dsa.set_id("dsa")
        Courses_Cache.cache[dsa.get_id()] = dsa

        stl = STL()
        stl.set_id("stl")
        Courses_Cache.cache[stl.get_id()] = stl

# main function
if __name__ == '__main__':
    Courses_Cache.load()

    sde = Courses_Cache.get_course("sde")
    print(sde.get_type())

    dsa = Courses_Cache.get_course("dsa")
    print(dsa.get_type())

    stl = Courses_Cache.get_course("stl")
    print(stl.get_type())


