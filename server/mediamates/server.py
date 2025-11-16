from typing import Union

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

# Create a FastAPI application instance
app = FastAPI()

# Define a Pydantic model for request body validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Define a GET endpoint at the root path "/"
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Define a GET endpoint with a path parameter and an optional query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Define a POST endpoint that accepts an Item object in the request body
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}

# Define a PUT endpoint to update an item, using both path parameter and request body
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "updated_item": item.dict()}

# static contents
app.mount('/static', StaticFiles(directory='static', html=True), name='static')

# Configure Jinja2Templates to find templates in the "templates" directory
templates = Jinja2Templates(directory="templates")

@app.get("/dynamic", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    return templates.TemplateResponse("item.html", {"request": request, "name": name})

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    return templates.TemplateResponse("home.html", {"request": request, "name": name})

@app.get("/login", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    return templates.TemplateResponse("login.html", {"request": request, "name": name})

@app.get("/user", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    return templates.TemplateResponse("user.html", {"request": request, "name": name})

@app.get("/connect", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    return templates.TemplateResponse("connect.html", {"request": request, "name": name})

@app.get("/matches", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    from match import find_matches

    matches = find_matches()

    return templates.TemplateResponse("matches.html", {"request": request, "matches": matches})

@app.post("/spotify")
async def read_item(request: Request, name: str = "Guest"):
    from spotify import get_playlist

    payload = await request.json()
    return get_playlist(payload['playlist_id'])

@app.post("/gemini")
async def read_item(request: Request, name: str = "Guest"):
    from gemini import evaluate

    payload = await request.json()
    return evaluate(payload['playlist'])
