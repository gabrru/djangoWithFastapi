from fastapi import FastAPI, Request
from django.contrib import admin
from django.urls import path
# from fastapi_asgi_middleware import FastapiMiddleware
from myapp.views import home

app = FastAPI()

@app.middleware("http")
async def fastapi_middleware(request: Request, call_next):
    response = await call_next(request)
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
]
