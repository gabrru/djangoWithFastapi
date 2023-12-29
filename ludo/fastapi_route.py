from fastapi import FastAPI
import django
import os
from myapp.controller.userController import create_user, get_all_User, update_user
from myapp.type.userType import IUser


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludo.settings")
django.setup()

app = FastAPI()

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


