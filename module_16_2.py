from fastapi import FastAPI, Path
from typing import Annotated
import asyncio
import fastapi
import uvicorn


app=FastAPI(swagger_ui_parameters=({"tryItOutEnabled": True}))

@app.get("/")
async def welcome():
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin():
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user(user_id: Annotated[int,Path(ge=1, le=100, description='Enter User ID', example='75')]):
    return {'message': f'Вы вошли как пользователь №{user_id}'}


@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str,Path(min_length=5, max_length=20,
                                      description='Enter username', example='Sergei')]
, age: Annotated[int,Path(ge=18, le=120, description='Enter age', example='52')]):
    return f'Информация о пользователе, Имя: {username}, Возраст: {age}'


if __name__ == '__main__': asyncio.run(uvicorn.run(app, host='127.0.0.1', port=8000, loop='asyncio'))