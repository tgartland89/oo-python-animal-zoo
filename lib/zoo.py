from lib.animal import Animal

class Zoo:
    all = []
    def __init__(self, name, location):
        self.name = name 
        self.location = location 
        Zoo.all.append(self)

# Adding the above __init__ will initialize zoo with a name and a location, which should both be passed as strings.
# name should return the name of the zoo instance.
# location should return the location of the zoo instance.
# Zoo.all should return an list of all the zoo instances.

    @property
    def animals(self):
        a_new_list =[]
        for animal in Animal.all:
            if animal.zoo == self:
                a_new_list.append( animal )
        # return a_new_list
        return [a for a in Animal.all if a.zoo == self ]

# the abovee @prop will return all the animals that a specific instance of a zoo has.

    @property
    def animal_species( self ):
        return list( { a.species for a in self.animals } )

# the above @prop returns a list of all the species (as strings) of the animals in the zoo. 
# However, if you have two dogs, it should only return one "Dog" string (aka an unique list)

    def find_by_species( self, species ):
        return [ a for a in self.animals if a.species == species ]
    
# the above def find_by_species will take in an animal's species as an argument and return an list 
# of all the animals in that zoo, which are of that species.

    @property
    def animal_nicknames( self ):
        return [ a.nickname for a in self.animals ]

# adding the above @prop for animal_nickname will return an list of all the nicknames of animals 
# that a specific instance of a zoo has.

    @classmethod
    def find_by_location( cls, loc ):
        return [ z for z in cls.all if z.location == loc ]

# adding the above @classmethod for find_by_loation will take in a location as an argument and return an 
# list of all the zoos within that location.