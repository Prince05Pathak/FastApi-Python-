from fastapi import FastAPI
from enum import Enum
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