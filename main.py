from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Hello World"}


@app.post("/")
async def post():
    return {"Message": "Hello from post route"}

@app.put("/")
async def put():
    return {"Message": "Hello from put route"}