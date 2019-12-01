
class User:
    def __init__(self, id_number, username, room=0):
        self.id = id_number
        self.username = username
        self.room = room

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value
