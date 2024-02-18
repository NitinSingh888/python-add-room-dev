class AddRoomResponseDto:
    def __init__(self):
        self.room = None
        self.response_status = None


@property
def room(self):
    return self._room


@room.setter
def room(self, value):
    self._room = value


@property
def response_status(self):
    return self._response_status


@response_status.setter
def response_status(self, value):
    self._response_status = value