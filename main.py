import os
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from users import auth
from common import views

BASEDIR = os.path.dirname(__file__)


app = FastAPI(
    title="Simple", debug=True
)
app.include_router(auth.auth_router)
app.include_router(views.common_router)

app.mount("/media", StaticFiles(directory=BASEDIR + "/media"), name="media")


@app.get('/')
async def hello_world():
    return {'msg': 'Hello World!'}
