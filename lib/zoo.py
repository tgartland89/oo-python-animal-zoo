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


# Imagine we have a zoo. A zoo is a place where different animals live. 
# The code helps us keep track of the animals in the zoo and perform some operations on them.

# In a zoo, we can have different animals like lions, tigers, and bears. 
# Each animal has a species (what kind of animal it is) and a nickname (a special name we give them).

# The code has a special class called "Zoo." 
# It helps us create and manage zoos. Inside the Zoo class, we have different functions (also called methods) that do specific things.

# The first function is called "init" we create a new zoo, this function is called automatically. 
# It asks for two pieces of information: the name of the zoo and its location. 
# For example, we could create a zoo called "Central Zoo" located in "New York."

# The next function is called "animals." 
# It gives us a list of all the animals in a specific zoo. 
# It looks at all the animals in the zoo and checks if they belong to that particular zoo. If they do, it adds them to the list.

# The third function is called "animal_species." 
# It gives us a list of all the different species of animals in the zoo. 
# But it only includes each species once. So if there are two dogs in the zoo, it will only say "Dog" once in the list.

# The fourth function is called "find_by_species." 
# If we tell it a specific animal species, like "Lion," it will give us a list of all the lions in the zoo.

# The fifth function is called "animal_nicknames." 
# It gives us a list of all the special names (nicknames) of the animals in the zoo.

# The last function is called "find_by_location." 
# If we tell it a specific location, like "New York," it will give us a list of all the zoos in that location.

# this code helps us create zoos, keep track of the animals in them, find specific animals or species, 
# and do other useful things with them.

