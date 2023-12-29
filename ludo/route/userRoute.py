from fastapi import APIRouter, FastAPI
import django
import os
from myapp.controller.userController import create_user, get_all_User, get_user, update_user
from myapp.type.userType import IUser


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludo.settings")
django.setup()

# router = APIRouter(prefix="/", tags=["choices"])

# app = FastAPI()
app = APIRouter(prefix="/user", tags=["choices"])

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with django!"}


@app.post("/create-user")
def createUser(data: IUser):
    return create_user(data)

@app.get("/get-all-user")
def getAllUser():
    return get_all_User()



@app.post("/update-user")
def updateUser(data: IUser):
    return update_user(data)

@app.get("/{user_id}")
def userData(user_id:int):
    return get_user(user_id)


