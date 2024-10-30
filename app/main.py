from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.post("/users")
async def create_user():
    return "Creando usuarios...."

@app.put("/users")
async def actualizando_user():
    return "Actualizando user...."