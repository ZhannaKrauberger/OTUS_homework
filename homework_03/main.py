from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "hello!"}


@app.get("/ping/")
def ping():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
