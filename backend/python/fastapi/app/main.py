from fastapi import FastAPI
from api.routes import character, chronology, localisation, user

app = FastAPI()

app.include_router(character.router)
app.include_router(chronology.router)
app.include_router(localisation.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI backend!"}