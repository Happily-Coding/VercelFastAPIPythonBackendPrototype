from fastapi import FastAPI, Query, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

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

@app.get("/")
async def root():
    return {"message": "Please use the post method on /test to get a result!"}
#return HTMLResponse(html)


@app.get("/test")
async def root():
    return {"message": "Please use the post method on /predict to get a useful result!"}



@app.post('/sendEmail')
async def send_email(email: str):
    print(f"Email would be sent to {email}")
    return {"message": "Email sent successfully", "email": email}
