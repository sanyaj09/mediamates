from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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

# Configure Jinja2Templates to find templates in the "templates" directory
templates = Jinja2Templates(directory="templates")

@app.get("/dynamic", response_class=HTMLResponse)
async def read_item(request: Request, name: str = "Guest"):
    # Render the "item.html" template with dynamic data
    return templates.TemplateResponse("item.html", {"request": request, "name": name})
