from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=200)
def hello_word():
    """Basic root endpoint"""
    return {"message": "well to sajeel"}
