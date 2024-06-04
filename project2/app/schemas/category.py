import re
from pydantic import field_validator
from app.schemas.base import CustomBaseModel

class Category(CustomBaseModel):
    name: str
    slug: str

    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Slug must contain only lowercase letters, dashes, and underscores')
        return value

class CategoryOutput(Category):
    id: int