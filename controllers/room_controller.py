from services.room_service import RoomService
from dtos.add_room_request_dto import AddRoomRequestDto
from dtos.add_room_response_dto import AddRoomResponseDto
from dtos.response_status import ResponseStatus


class RoomController():
    def __init__(self, room_service: RoomService):
        self.room_service = room_service

    def add_room(self, request_dto: AddRoomRequestDto) -> AddRoomResponseDto:

        response_dto: AddRoomResponseDto = AddRoomResponseDto()

        try:
            room = self.room_service.add_room(
                user_id=request_dto.user_id,
                room_name=request_dto.room_name,
                description=request_dto.description,
                room_type=request_dto.room_type,
                price=request_dto.price
            )

            response_dto.response_status = ResponseStatus.SUCCESS
            response_dto.room = room

        except Exception:
            response_dto.response_status = ResponseStatus.FAILURE

        return response_dto

