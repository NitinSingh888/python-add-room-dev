from typing import Optional


class BaseModel:
    def __init__(self):
        self._id: Optional[int] = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id