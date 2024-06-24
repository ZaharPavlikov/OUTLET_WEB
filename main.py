from fastapi import FastAPI, HTTPException, Depends, Request,Form,status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_api(request: Request):
    return templates.TemplateResponse("index.html",{"request": request}) 
