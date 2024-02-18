from models.base_model import BaseModel


class Room(BaseModel):
    def __init__(self, room_name=None, price=0.0, room_type=None, description=''):
        super().__init__()
        self._room_name = room_name
        self._price = price
        self._room_type = room_type
        self._description = description

    @property
    def room_name(self):
        return self._room_name

    @room_name.setter
    def room_name(self, value):
        self._room_name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value




