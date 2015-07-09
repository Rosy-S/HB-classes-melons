"""This file should have our melon-type classes in it."""

class Melons(object):   

    def get_base_price(self): 
        return 5.0

    def get_price(self):
        try:
            self.get_price()
        except:
            print "Cannot use that method"



class Watermelon(Melons):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price()

        if qty > 3:
            total_cost *= .75

        return total_cost

class Cantaloupe(Melons):
    species ='Cantaloupe'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']
    
    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price()

        if qty > 5:
            total_cost *= .5

        return total_cost


class Casaba(Melons):

    species = 'Casaba'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    
    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * (self.get_base_price() + 1) * 1.5

        return total_cost


class Sharlyn(Melons):
    species= 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price() * 1.5

        return total_cost

class SantaClaus(Melons):
    species = 'Santa Claus'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price() * 1.5

        return total_cost

class Christmas(Melons):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price() 

        return total_cost

class HornedMelon (Melons):
    species = 'Horned Melon'
    color = 'yellow'
    imported =  True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price() * 1.5

        return total_cost

class Xigua(Melons): 
    species ='Xigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * self.get_base_price() * 3.5

        return total_cost


class Ogen(Melons):
    species = 'Ogen'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total_cost = qty * (self.get_base_price() + 1)

        return total_cost