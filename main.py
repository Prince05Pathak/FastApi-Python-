from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()
'''
@app.get("/")
async def root():
    return {"Message": "Hello World"}


@app.post("/")
async def post():
    return {"Message": "Hello from post route"}

@app.put("/")
async def put():
   return {"Message": "Hello from put route"}
'''
# Path Parameter in Fast api
'''@app.get("/users")
async def list_users():
    return {"Message": "List user route"}

@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/food_name")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You are eating vegetables"}
    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "You are eating fruits"}

    return{
        "food_name": food_name,
        "message": "I like dairy products"
    }
'''
#Query Parameters
fake_items_db = [{"item_name": "Foo"},{"item_name": "For"},{"item_name": "Fro"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get("/items/{item_id}")
async def get_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
            item.update(
            {
                "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sit."
            }
            )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_items(user_id: int, item_id: str, q: str | None, short: bool = False):
     item = {"item_id": item_id, "owner_id": user_id}
     if q:
         item.update({"q": q})
     if not short:
         item.update(
             {
                 "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sit."
             }
         )
     return item