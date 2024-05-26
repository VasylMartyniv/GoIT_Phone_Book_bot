# Клас для представлення нотатки з ідентифікатором, текстом та тегами
class Note:
    def __init__(self, id, text, tags):
        self.id = id
        self.text = text
        self.tags = tags
