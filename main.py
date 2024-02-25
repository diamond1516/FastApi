from fastapi import FastAPI
from users import auth

app = FastAPI(
    title="Simple", debug=True
)
app.include_router(auth.auth_router)


@app.get('/')
async def hello_world():
    return {'msg': 'Hello World!'}
