from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def admin() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    new_index = str(int(max(users, key=int)) + 1)
    users[new_index] = f'Имя: {username}, возраст: {age}'
    return f"User {new_index} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(ge=1, le=100, description="Enter User ID")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def admin(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    users.pop(str(user_id))
    return f"The user {user_id} was deleted"
