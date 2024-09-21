from fastapi import FastAPI, Path, HTTPException, Request
from typing import Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


class User(BaseModel):
    id: int = None
    username: str
    age: int


app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{user_id}')
async def get_user(request: Request,
                   user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> HTMLResponse:
    for i in range(len(users)):
        if users[i].id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": users[i]})
    raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    if users:
        new_user = User(id=users[-1].id + 1, username=username, age=age)
    else:
        new_user = User(id=1, username=username, age=age)
    users.append(new_user)
    return f"User {users[-1].id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f"The user {user_id} is registered"
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> str:
    for i in range(len(users)):
        if users[i].id == user_id:
            users.pop(i)
            return f"The user {user_id} was deleted"
    raise HTTPException(status_code=404, detail="User was not found")
