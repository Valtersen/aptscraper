import views
from fastapi import FastAPI

app = FastAPI()

app.include_router(views.router)


@app.get("/")
async def read_root():
    return {"Hello": "Go to '/api/apartments/' or /api/apartments/filter/"}
