from fastapi import APIRouter, FastAPI
import django
import os
from myapp.type.commonType import Titem
from myapp.controller.itemController import create_item, get_all_item, user_all_item


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludo.settings")
django.setup()

# app = FastAPI()
app = router = APIRouter(prefix="/item", tags=["choices"])

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with django!"}


@app.post("/create-item")
def createUser(data: Titem):
    return create_item(data)

@app.get("/get-all-item")
def getAllUser():
    return get_all_item()

@app.get("/user-all-item")
def getAllUser():
    user_id = 1
    return user_all_item(user_id)



# @app.post("/update-user")
# def updateUser(data: IUser):
#     return update_user(data)


