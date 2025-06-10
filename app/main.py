from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/submit")
async def submit(data: dict):
    # Process the submitted data
    return {"message": "Data received", "data": data}
