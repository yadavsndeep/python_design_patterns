from enum import Enum
from abc import abstractmethod

class Location(Enum):
    INDOOR = 1
    OUTDOOR = 2

class Surface(Enum):
    GRASS = 1
    HARD = 2
    TURF = 3
    OTHER = 4



class Sport:

    def __init__(self,name, surface, location, player_count ):
        self.name = name
        self.surface = surface
        self.location = location
        self.player_count = player_count



class Specification:
    def __init__(self, sport):
        pass

    def __and__(self,other):
        return AndSpecification(self,other)

    @abstractmethod
    def is_satisfied(self, sport):
        pass


class LocationSpecification(Specification):

    def __init__(self, location):
        self.location = location

    def is_satisfied(self, sport):
        return self.location == sport.location



class SurfaceSpecification(Specification):

    def __init__(self,surface):
        self.surface = surface

    def is_satisfied(self, sport):
        return self.surface == sport.surface


class PlayerSpecification(Specification):

    def __init__(self,player_count):
        self.player_count = player_count

    def is_satisfied(self, sport):
        return self.player_count == sport.player_count



class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, sport):
        return  all(map(lambda spec: spec.is_satisfied(sport) , self.args))





class Filter:

    def filter(self, sports, spec):
        pass



class FilterImpl(Filter):

    def filter(self, sports, spec):
        for sport in sports:
            if spec.is_satisfied(sport):
                yield sport

def main():
    football = Sport('Football', Surface.GRASS, Location.OUTDOOR, 11)
    basketball = Sport('Basketball', Surface.HARD, Location.INDOOR, 5)
    hockey = Sport('Hockey', Surface.TURF, Location.OUTDOOR, 11)
    futsal = Sport('Futsal', Surface.OTHER, Location.INDOOR, 7)

    sports = [football, hockey,basketball,futsal]

    filter_tool = FilterImpl()

    outdoor = LocationSpecification(Location.OUTDOOR)
    for s in filter_tool.filter(sports,outdoor):
        print(f' - {s.name} is played Outdoors')

    for s in filter_tool.filter(sports, SurfaceSpecification(Surface.HARD)):
        print(f' - {s.name} is played on Hard surface')

    for s in filter_tool.filter(sports, PlayerSpecification(11)):
        print(f' - {s.name} is played with 11 players')


    ind_and_other = SurfaceSpecification(Surface.OTHER) & LocationSpecification(Location.INDOOR)

    for s in filter_tool.filter(sports, ind_and_other):
        print(f' - {s.name} is played indoor and neither on Hard or Turf surfaces')



if __name__ ==  '__main__':
    main()