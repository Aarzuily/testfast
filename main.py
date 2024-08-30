from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Inputtxt(BaseModel):
    text: str

class Outpttxt(BaseModel):
    processed_text: str

@app.post("/process_text/", response_model=Outpttxt)

async def process_text(request: Inputtxt):
    capitalized_text = request.text.upper()
    return Outpttxt(processed_text=capitalized_text)
