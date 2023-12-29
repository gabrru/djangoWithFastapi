from fastapi import FastAPI
from .userRoute import app as user_api
from .commonRoute import app as common_api

__all__ = ("register_routers",)


def register_routers(app: FastAPI):
    app.include_router(user_api)
    app.include_router(common_api)
    
    
    
