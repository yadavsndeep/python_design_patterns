'''
This script demonstartes creation of objects using Builder pattern
Advantages:
Reusability: While making the various representations of the products, we can use the same construction code for other representations as well.
Single Responsibility Principle: We can separate out both the business logic as well as the complex construction code from each other.
Construction of the object: Here we construct our object step by step, defer construction steps or run steps recursively.
Disadvantages:
Code complexity increases: The complexity of our code increases, because the builder pattern requires creating multiple new classes.
Mutability: It requires the builder class to be mutable
Initialization: Data members of the class are not guaranteed to be initialized.
'''
from abc import ABC, abstractmethod


class Sport(ABC):
    def __init__(self):
        self.build_team()

    @abstractmethod    
    def build_team(self):
        raise NotImplementedError


    def __repr__(self):
            outdoor = 'Outdoors' if self.outdoor_flag == True else 'Indoors'
            return f'{self.name!r} has {self.player_count!r} players and is usually played {outdoor!r} for {self.duration!r} minutes'





class Football(Sport):

    def build_team(self):
        self.name = 'Football'
        self.duration = 90
        self.player_count = 11
        self.outdoor_flag = True


class Basketball(Sport):
    def build_team(self):
        self.name = 'Basketball'
        self.duration = 60
        self.player_count = 5
        self.outdoor_flag = False


class Boxing(Sport):

    def build_team(self):
        self.name = 'Boxing'
        self.duration = 12
        self.player_count = 2
        self.outdoor_flag = False
        self.contact_flag = True

    def __repr__(self):
        outdoor = 'Outdoors' if self.outdoor_flag == True else 'Indoors'
        return f'{self.name!r} has {self.player_count!r} players and is usually played {outdoor!r} for {self.duration!r} minutes. It is a Contact Sport- {self.contact_flag}.'



def main():
    football = Football()
    print(football)

    basketball = Basketball()
    print(basketball)
    
    boxing = Boxing()
    print(boxing)



if __name__ == "__main__" :
    main()


    