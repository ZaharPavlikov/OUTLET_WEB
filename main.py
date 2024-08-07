from fastapi import FastAPI, HTTPException, Depends, Request,Form,status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from fastapi_users import fastapi_users, FastAPIUsers


app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_api(request: Request):
    return templates.TemplateResponse("index.html",{"request": request}) 

@app.post("/search_product")
async def search_product(product_name = Form()):
    return {"Name of product = ": product_name}
