from fastapi import FastAPI, Form, Depends


class SampleForm:
    def __init__(self,
                username: str = Form(...),
                password: str = Form(...)):
        self.username = username
        self.password = password



app = FastAPI()

@app.get("/predict")
def test():
    return{"value":"test value"}

@app.post("/predict")
async def predict(form: SampleForm = Depends()):
    print(form)
    return form