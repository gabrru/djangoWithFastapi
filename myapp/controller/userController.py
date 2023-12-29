from django.forms import model_to_dict
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from myapp import models as django_models
from myapp.type.userType import IUser


def create_user(user: IUser):
    try:
        new_user = django_models.Customer(**user.dict())
        new_user.save()
        return JSONResponse(content={"message": "Item created successfully"}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
def get_all_User():
    try:
        data = django_models.Customer.objects.all()
        data = list(data.values())
        return {"data" : data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def update_user(user:IUser):
    try:
        user = django_models.Customer.objects.get(id = user.id)
        user.name = user.name
        user.age = user.age
        user.save()
        return {"data": "User updated successfully "}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_user(user_id : int):
    try:
        print("user_id-------------", user_id)
        user = django_models.Customer.objects.get(id=user_id)
        user = model_to_dict(user, exclude=['_state'])
        print("user-data----------", user)
        return user
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



