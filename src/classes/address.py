from src.classes.field import Field


class Address(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return self.value

    def change_address(self, old_address: str, new_address: str):
        if self.value and self.value == old_address:
            self.value = new_address
        else:
            raise ValueError("ERROR: There is no such address")
