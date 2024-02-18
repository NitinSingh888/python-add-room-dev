from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, name=None, password=None, phone=None, user_type=None):
        super().__init__()
        self.name = name
        self.password = password
        self.phone = phone
        self.user_type = user_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

