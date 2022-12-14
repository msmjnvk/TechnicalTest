from typing import List
from fastapi import FastAPI, Depends, Body
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
from app.model import UserSchema, UserLoginSchema,RequestSchema,ResponseSchema
from auth.jwt_bearer import JWTBearer
from auth.jwt_handler import signJWT


app = FastAPI()
users = []

@app.post("/get-phone-country",tags=["Contry Details"], dependencies=[Depends(JWTBearer())])
async def get_phone_contry(request: RequestSchema = Body(...)):
    return ResponseSchema(Phone=request.Phone,
    Country=region_code_for_country_code(phonenumbers.parse(request.Phone).country_code)
    )


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False
