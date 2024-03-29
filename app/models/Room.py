
# Global for all to use.
DIRECTIONS = ["North", "East", "South", "West", "Up", "Down"]


class Room:
    def __init__(self, id_number, name, description="A simple room", exits={}):
        self.id = id_number
        self.name = name
        self.description = description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
