import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel

class User(CustomBaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid Username')
        return value