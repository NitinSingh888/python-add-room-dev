from models.room import Room
from abc import ABC, abstractmethod
from repositories.room_repository import RoomRepository
from repositories.user_repository import UserRepository
from exceptions.user_not_found_error import UserNotFoundError
from exceptions.unauthorized_access_error import UnAuthorizedAccessError
from models.user_type import UserType
from models.room_type import RoomType


class RoomService(ABC):

    def __init__(self, room_repository: RoomRepository, user_repository: UserRepository):
        self.room_repository = room_repository
        self.user_repository = user_repository

    @abstractmethod
    def add_room(self, user_id: int, room_name: str, price: float, room_type: str, description: str) -> Room:
        pass


class RoomServiceImpl(RoomService):

    def __init__(self, room_repository: RoomRepository, user_repository: UserRepository):
        super().__init__(room_repository, user_repository)

    def add_room(self, user_id: int, room_name: str, price: float, room_type: str, description: str) -> Room:
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise UserNotFoundError("User not found")

        if user.user_type != UserType.ADMIN:
            raise UnAuthorizedAccessError("User is not an admin")

        room = Room(
            room_name=room_name,
            price=price,
            room_type=RoomType(room_type),
            description=description
        )

        saved = self.room_repository.save(room)
        return saved

