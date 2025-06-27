import shutil
import os
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.blip_captioner import generate_caption 
from models.text_qa import ask_openai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}

def validate_image_file(file: UploadFile) -> None:
    """Validate uploaded image file"""
    if file.size and file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large. Maximum size is 10MB.")
    
    if file.filename:
        file_ext = os.path.splitext(file.filename.lower())[1]
        if file_ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
            )

@app.post("/ask")
async def ask(image: UploadFile = File(...), question: str = Form(...)):
    validate_image_file(image)
    
    if not question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    image_path = None
    try:
        import uuid
        file_ext = os.path.splitext(image.filename)[1] if image.filename else ".jpg"
        temp_filename = f"temp_{uuid.uuid4()}{file_ext}"
        image_path = temp_filename
        
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        caption = generate_caption(image_path)
        if not caption or caption.startswith("Something went wrong"):
            raise HTTPException(status_code=500, detail="Failed to generate image caption")
        
        response = ask_openai(caption, question)
        if not response or response.startswith("OpenAI API key not configured"):
            raise HTTPException(status_code=500, detail="Failed to get answer from AI")

        return {
            "caption": caption,
            "question": question,
            "answer": response
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        if image_path and os.path.exists(image_path):
            try:
                os.remove(image_path)
            except Exception as e:
                print(f"Warning: Failed to clean up temporary file {image_path}: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Image Q&A service is running"}
        
