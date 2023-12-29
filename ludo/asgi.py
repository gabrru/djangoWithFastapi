"""
ASGI config for ludo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.conf import settings
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludo.settings")

# django_asgi_app = get_asgi_application()
application = get_asgi_application()
# from .route.userRoute import app as user_api
# from .route.commonRoute import app as common_api


# async def application(scope, receive, send):
#     if scope["type"] == "http" and "/admin/" in scope["path"]:
#         await django_asgi_app(scope, receive, send)
#     elif scope["type"] == "http" and "/user/" in scope["path"]:
#         await user_api(scope, receive, send)
#     elif scope["type"] == "http":
#         await common_api(scope, receive, send)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .route.router import register_routers

fastapp = FastAPI()
# application = WhiteNoise(application, root="/path/to/static/files")
# application.add_files("/path/to/more/static/files", prefix="more-files/")

def init(app: FastAPI):

    register_routers(app)
    if settings.MOUNT_DJANGO_APP:
        fastapp.mount("/", application)
        fastapp.mount("/static", StaticFiles(directory="staticfiles"), name="static")


init(fastapp)




