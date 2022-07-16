from fastapi import FastAPI, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import joblib 
import json 




class SampleForm:
    def __init__(self,
                num1: int = Form(...),
                num2: int = Form(...)):
        self.num1 = num1
        self.num2 = num2

col_data = joblib.load("coldata_serial.z")
test_data = {
    "this": "this",
    "that": "that"
}
app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/predict")
async def test():
    return jsonable_encoder(col_data)

@app.post("/predict")
async def predict(form: SampleForm = Depends()):
    return form.num1 + form.num2