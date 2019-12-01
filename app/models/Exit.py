

class Exit:
    def __init__(self, room_one_id, room_two_id, locked=False):
        self.room_one_id = room_one_id
        self.room_two_id = room_two_id
        self.locked = locked

    @property
    def locked(self):
        return self.__locked

    @locked.setter
    def locked(self, value):
        self.__locked = value
