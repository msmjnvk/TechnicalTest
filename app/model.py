from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Joe Eric",
                "email": "joe@example.com",
                "password": "Hello123"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@example.com",
                "password": "Hello123"
            }
        }

class RequestSchema(BaseModel):
    Phone: str

    class Config:
        schema_extra = {
            "example": {
                "Phone": "+919999999999"
            }
        }

class ResponseSchema(BaseModel):
    Phone: str
    Country: str

    class Config:
        schema_extra = {
            "example": {
                "Phone": "+919999999999",
                "Country": "IN"
            }
        }