

class Pokemon:

    def __init__(self, id_num, name="A new pokemon", description="A Pokemon", type_one=0, type_two=None):
        self.id = id_num
        self.name = name
        self.description = description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
