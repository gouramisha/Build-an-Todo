#
from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.podt("/create_user",status_code =status.HTTp_201_created)
def create_user():
    return{
        "message": "User Created"
    }
