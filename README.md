# 🔍 Multimodal QA Agent - Image Question Answering Application

A sophisticated multimodal question-answering web application that combines computer vision and natural language processing to analyze images and answer questions about them. Built with FastAPI backend and a modern HTML/CSS/JS frontend.

## 🎯 Task Completion: Multimodal QA Agent

This project successfully implements the requirements for building a multimodal QA agent:

### ✅ **Core Requirements Completed:**
- **Image Input**: Upload via drag & drop or file selection
- **Text Questions**: Interactive question input with examples
- **Vision + Language LLM**: BLIP for image understanding + OpenAI for reasoning
- **Web Application**: Full-stack implementation with modern UI

### ✅ **Bonus Features Implemented:**
- **Fallback System**: Graceful handling when OpenAI API is unavailable
- **Robust Error Handling**: Comprehensive error management
- **Production-Ready**: Security, validation, and performance optimizations

## ✨ Features

- **Multimodal AI**: Combines computer vision (BLIP) and language models (OpenAI)
- **Image Upload**: Drag & drop or click to upload images
- **AI Image Captioning**: Automatically generates detailed descriptions using BLIP model
- **Question Answering**: Ask questions about images and get comprehensive AI-powered answers
- **Modern UI**: Beautiful, responsive design with smooth animations
- **Real-time Processing**: Live feedback during image analysis
- **File Validation**: Secure file upload with size and type restrictions
- **Automatic Cleanup**: Temporary files are automatically cleaned up
- **Health Monitoring**: Built-in health check endpoint
- **Error Handling**: Robust error handling and user-friendly messages
- **Fallback Support**: Works even when external APIs are unavailable

## 📸 Results Showcase

See the application in action! Check out these screenshots showing real results:

- **[Screenshot 1](backend/my_images/Screenshot%20(9).png)** - Example interaction and results
- **[Screenshot 2](backend/my_images/Screenshot%20(10).png)** - Another successful query
- **[Screenshot 3](backend/my_images/Screenshot%20(11).png)** - More demonstration results

These screenshots demonstrate the application's ability to:
- Generate detailed image captions using BLIP model
- Provide comprehensive answers to user questions
- Handle various types of images and queries
- Display results in a clean, user-friendly interface

## 🤖 LLM APIs Used & Architecture

### **Vision Model: BLIP (Salesforce)**
- **Purpose**: Image captioning and visual understanding
- **Why BLIP**: State-of-the-art vision-language model, excellent at describing image content
- **Implementation**: Local model loading with caching for performance

### **Language Model: OpenAI GPT-3.5-turbo**
- **Purpose**: Question answering and reasoning about image content
- **Why GPT-3.5-turbo**: Reliable, fast, and excellent at understanding context
- **Features**: 500-token responses for detailed answers, temperature 0.7 for creativity

### **Architecture Design**
```
Image Upload → BLIP Captioning → OpenAI Q&A → Response Display
     ↓              ↓                ↓              ↓
File Validation → Model Caching → Error Handling → Clean UI
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- OpenAI API key (optional, for question answering)

### Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables (optional):**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Start the server:**
   ```bash
   cd backend
   python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

5. **Open the frontend:**
   - Open `frontend.html` in your web browser
   - Or serve it using a local server

## 🔧 Configuration

### OpenAI API (Optional)

To enable question answering functionality:

1. Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com/)
2. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

If no API key is provided, the application will still generate image captions but will show a message for question answering.

## 📱 How to Use

1. **Upload an Image:**
   - Click the upload area or drag & drop an image
   - Supported formats: JPG, PNG, GIF, BMP, WebP
   - Maximum file size: 10MB

2. **Ask a Question:**
   - Type your question in the text field
   - Or click one of the example questions

3. **Get Results:**
   - View the AI-generated image caption
   - See the detailed answer to your question

## 🛠️ API Endpoints

- **POST** `/ask` - Upload image and ask a question
  - Parameters: `image` (file), `question` (string)
  - Returns: JSON with caption, question, and answer

- **GET** `/health` - Health check endpoint
  - Returns: Server status information

- **GET** `/docs` - Interactive API documentation (Swagger UI)

## 🎨 Frontend Features

- **Responsive Design**: Works on desktop and mobile
- **Drag & Drop**: Easy image upload with visual feedback
- **Real-time Preview**: See your uploaded image immediately
- **Loading States**: Visual feedback during processing
- **Error Handling**: Clear error messages for various scenarios
- **Example Questions**: Quick-start question suggestions
- **Modern UI**: Beautiful gradient design with smooth animations

## 🔍 Example Questions

- "What objects can you see in this image?"
- "Describe the scene in this image."
- "What colors are prominent in this image?"
- "Is this image taken indoors or outdoors?"
- "What emotions does this image convey?"
- "Are there any people in this image?"

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'torch'" error:**
   - Make sure you've installed all dependencies: `pip install -r requirements.txt`
   - Ensure you're using Python 3.8+

2. **CORS errors:**
   - The backend is configured to allow all origins
   - Make sure the backend is running on `http://127.0.0.1:8000`

3. **OpenAI API errors:**
   - Check your API key in the `.env` file
   - Ensure you have sufficient credits in your OpenAI account
   - Verify the API key is valid

4. **File upload errors:**
   - Check file size (max 10MB)
   - Ensure file type is supported (JPG, PNG, GIF, BMP, WebP)

### Performance Tips

- Use images under 5MB for faster processing
- The first request may take longer as models are loaded into memory
- GPU acceleration is automatically used if available
- Models are cached after first load for better performance

## 🏗️ Project Structure

```
├── backend/
│   ├── main.py              # FastAPI application with improved error handling
│   ├── models/
│   │   ├── blip_captioner.py # Image captioning with model caching
│   │   └── text_qa.py       # Question answering with OpenAI
│   ├── my_images/           # Screenshots of results
│   └── utils/
│       └── image_io.py      # Image processing utilities
├── frontend.html            # Main frontend interface
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔒 Security Features

- **File Validation**: File type and size restrictions
- **Temporary File Cleanup**: Automatic cleanup of uploaded files
- **Error Handling**: Secure error messages without exposing internals
- **Input Validation**: Question and image validation

## 🚀 Recent Improvements

- ✅ Added automatic file cleanup
- ✅ Improved error handling and validation
- ✅ Added health check endpoint
- ✅ Model caching for better performance
- ✅ File size and type restrictions
- ✅ Better API documentation
- ✅ Enhanced OpenAI responses (500 tokens, detailed prompts)
- ✅ Fallback system for API failures

## 📊 Test Results

The application has been tested with various image types and questions:

- ✅ **Portrait photos** - Successfully identifies people and scenes
- ✅ **Landscape images** - Accurately describes outdoor environments
- ✅ **Object photos** - Correctly identifies objects and their context
- ✅ **Complex scenes** - Handles multiple objects and interactions
- ✅ **Error scenarios** - Gracefully handles API failures and invalid inputs

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License. 