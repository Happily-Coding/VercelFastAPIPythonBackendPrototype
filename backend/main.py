from fastapi import FastAPI, Query, __version__ , Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any
import bard_predictor
from fastapi import FastAPI, UploadFile
from typing import Optional
import uvicorn
from os import getenv

app = FastAPI()

if __name__ == "__main__":
    port = int(getenv('PORT',8000))
    uvicorn.run("main:app",port=port,reload=True)


#app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
        </div>
    </body>
</html>
"""

@app.get("/advancedtest")
async def advanced_test():
    return HTMLResponse(html)

@app.get("/test")
async def test():
    return {"message": "Please use the post method on /predict to get a useful result!"}



# Load environment variables from .env file in this folder (if any)
load_dotenv()

@app.post("/predict", response_model = Response) #Prepare an endpoint in /predict
async def predict(
    question: Optional[str] = Form(None), #Get the value in the key question from the form inside the request body, otherwise None. Automatically validate that its a string.
    file: Optional[UploadFile] = Form(None) #Get the value in the key file from the form inside the request body, otherwise None. Automatically validate that its an UploadFile
    ) -> Any:

    result = bard_predictor.predict(question) if question else 'Please provide a question!'
    return {'result':result} #Response model response means we have to return a dictionary