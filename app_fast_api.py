import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Text": "Hello, I'm FastAPI"}

@app.get("/ping")
def read_root():
    return {"pong":"ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)