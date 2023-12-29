from django.forms import model_to_dict
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from myapp.type.commonType import Titem
from myapp import models as django_models


def create_item(item):
    try:
        customer = django_models.Customer.objects.get(id=item.customer)
        id  = item.customer
        # print("customer-------", id.dict())       
        new_item = django_models.Item(customer = customer,title = item.title, description = item.description, amount = item.amount)

        new_item.save()
        return JSONResponse(content={"message" : "Your item add successfully!!"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
def get_all_item():
    try:
        item = django_models.Item.objects.all()
        item = list(item.values())
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
def user_all_item(user_id : int):
    try:
        customer = django_models.Customer.objects.get(id=user_id)
        item = django_models.Item.objects.select_related("customer").filter(customer = user_id)
        # item = [p for p in django_models.Item.objects.select_related("customer").filter(customer = user_id)]
        # print("item--------------------", item)
        # data = []
        # for p in item:
        #     user = item._state.fields_cache["customer"]
        #     print("user-----------------", user)
        #     userData = model_to_dict(p, exclude=['._state.fields_cache["customer"]'])
        #     print("data????????????????", userData)
        #     data.append(userData)
        # # data = model_to_dict(item.values(), exclude=['_state'])
        item = list(item)
        print("list item--------------------", item)
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



