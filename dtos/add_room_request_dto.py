from models.room_type import RoomType
from typing import Optional


class AddRoomRequestDto:
    def __init__(self, user_id, room_name, price, room_type, description):
        self.user_id = user_id
        self.room_name = room_name
        self.price = price
        self.room_type = room_type
        self.description = description

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

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
