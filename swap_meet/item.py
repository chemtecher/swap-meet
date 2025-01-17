# create an`Item` class
# create an attribute named `category`, which is an empty string by default
# Make category an optionally keyword argument to pass for Item 


class Item:
    def __init__(self, category=None, condition = 0 ):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
    
    def __str__(self):
        return "Hello World!"


    
        
# - All three classes and the `Item` class have an instance method named `condition_description`, 
# which should describe the condition in words based on the value, assuming they all range from 0 to 5. 
# These can be basic descriptions 
# (eg. 'mint', 'heavily used') but feel free to have fun with these (e.g. 'You probably want a glove for this one..."). 
# The one requirement is that the `condition_description` for all three classes above have the same behavior.
 

    def condition_description(self):
        if 0 <= self.condition < 2:
            return "Hard Pass!"
        elif 2 <= self.condition < 3:
            return "Its seen better days!"
        elif 3 <= self.condition < 4:
            return " A little loved"
        elif 4 <= self.condition < 5:
            return "Slighty used"
        elif self.condition == 5:
            return "Mint"
        
        
