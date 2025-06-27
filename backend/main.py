import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from models.blip_captioner import generate_caption 
from models.text_qa import ask_openai
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origin = ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(image : UploadFile = File(...), question : str = Form(...)):
    try:
        image_path = f"temp_{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        caption : str = generate_caption(image_path)
        response = ask_openai(caption, question)    

        return {
            "caption": f"{caption}",
            "question": f"{question}",
            "answer ": f"{response}"
        }

    except Exception as e:
        return {"error :", str(e)}
        
