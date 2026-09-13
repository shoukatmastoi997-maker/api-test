from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return {"Yes bro, I am here to help you!"}
@app.get("/hello")
def hello(): 
    return {"Hello bro, How are you?"}
@app.get("/shoukat")
def shoukat():
    return {"Shoukat bro, I am here to help you!"}