from src.classes.field import Field

class Phone(Field):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value
    