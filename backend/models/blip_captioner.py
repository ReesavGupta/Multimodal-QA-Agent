import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

_processor = None
_model = None
_device = None

def _load_model():
    """Load and cache the BLIP model and processor"""
    global _processor, _model, _device
    
    if _processor is None or _model is None:
        _device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Loading BLIP model on device: {_device}")
        
        try:
            _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
            _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
            _model = _model.to(_device)
            print("BLIP model loaded successfully")
        except Exception as e:
            print(f"Error loading BLIP model: {str(e)}")
            raise

def generate_caption(image_path: str) -> str:
    """Generate caption for the given image"""
    try:
        _load_model()
            
        if not os.path.exists(image_path):
            return "Error: Image file not found"
        
        image = Image.open(image_path).convert("RGB")
        
        inputs = _processor(images=image, return_tensors="pt")
        inputs = {k: v.to(_device) for k, v in inputs.items()}
        
        with torch.no_grad():
            output = _model.generate(**inputs, max_length=50, num_beams=5)
        
        caption = _processor.decode(output[0], skip_special_tokens=True)
        
        return caption if caption.strip() else "No caption generated"
        
    except Exception as e:
        error_msg = f"Error generating caption: {str(e)}"
        print(error_msg)
        return error_msg
