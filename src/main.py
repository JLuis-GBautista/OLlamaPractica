from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = os.path.join(os.path.dirname(__file__), "../public", "index.html")
    with open(index_path, "r") as file:
        content = file.read()
    return HTMLResponse(content=content)