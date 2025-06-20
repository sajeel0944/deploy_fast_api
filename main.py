from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_word():
    """Basic root endpoint"""
    return {"message": "well to sajeel"}



@app.get("/new")
def hello_word():
    """Basic root endpoint"""
    return {"message": "new user in login"}


@app.post("/post")
def hello_word():
    """Basic root endpoint"""
    return {"message": "this is post request"}



@app.put("/put")
def hello_word():
    """Basic root endpoint"""
    return {"message": "this is put request"}



@app.delete("/delete")
def hello_word():
    """Basic root endpoint"""
    return {"message": "this is delete request"}

