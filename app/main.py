from fastapi import FastAPI

from app.endpoints.user import user_endpoints

app = FastAPI(
    title="User Management API",
    description="API for managing users",
    version="1.0.0",
)

app.include_router(user_endpoints.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
