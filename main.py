from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='review de filmes')

app.mount("/static",StaticFiles(directory='static'),name='static')

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(
        request=request,name="index.html"
    )