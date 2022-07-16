from fastapi import FastAPI, Form, Depends


class SampleForm:
    def __init__(self,
                num1: int = Form(...),
                num2: int = Form(...)):
        self.num1 = num1
        self.num2 = num2



app = FastAPI()

@app.get("/predict")
def test():
    return{"value":"test value"}

@app.post("/predict")
async def predict(form: SampleForm = Depends()):
    return form.num1 + form.num2