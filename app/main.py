from fastapi import FastAPI

from app.endpoints import user_endpoints

app = FastAPI()

app.include_router(user_endpoints.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
