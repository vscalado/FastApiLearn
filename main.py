from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator('email')
    def validate_email(cls,value):
        if '@' not in value:
            raise ValueError('Invalid email')
        return value
    
def f(user:User):
    user.email
    pass

user = User(name='Vitor Calado', age=25, email='vitorcalado@gmail.com')
print(user)
