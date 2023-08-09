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


class Sport():
    def __init__(self):
        self.name = None
        self.player_count = 11
        self.outdoor_flag = True
        self.duration = 0


    def __repr__(self):
            outdoor = 'Outdoors' if self.outdoor_flag == True else 'Indoors'
            return f'{self.name!r} has {self.player_count!r} players and is usually played {outdoor!r} for {self.duration!r} minutes'





class TeamBuilder(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod    
    def build_team(self):
        raise NotImplementedError


class Football(TeamBuilder):
    def __init__(self):
        self.sport = Sport()

    def reset(self):
        self.sport = Sport()

    def build_team(self):
        self.sport.name = 'Football'
        self.sport.duration = 90

    def get_team(self):
        return self.sport

class Basketball(TeamBuilder):
    def __init__(self):
        self.sport = Sport()

    def reset(self):
        self.sport = Sport()

    def build_team(self):
        self.sport.name = 'Basketball'
        self.sport.duration = 60
        self.sport.player_count = 5
        self.sport.outdoor_flag = False

    def get_team(self):
        return self.sport

class Boxing(TeamBuilder):
    def __init__(self):
        self.sport = Sport()

    def reset(self):
        self.sport = Sport()

    def build_team(self):
        self.sport.name = 'Boxing'
        self.sport.duration = 12
        self.sport.player_count = 2
        self.sport.outdoor_flag = False
        self.sport.contact_flag = True

    def get_team(self):
        print(f'{self.sport.name} is a Contact Sport- {self.sport.contact_flag}.')
        return self.sport


def main():
    football = Football()
    football.build_team()

    print(football.get_team())

    basketball = Basketball()
    basketball.build_team()

    print(basketball.get_team())
    
    boxing = Boxing()
    boxing.build_team()

    print(boxing.get_team())



if __name__ == "__main__" :
    main()


    