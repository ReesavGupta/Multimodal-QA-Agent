from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin = ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(image : UploadFile = File(...), question : str = Form(...)):
    try:
        image_bytes = await image.read()
    except Exception as e:
        return {"error :", str(e)}
        
