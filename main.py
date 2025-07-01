from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from ibm_granite_utils import query_granite
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def homepage():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
async def chat_ai(request: Request):
    data = await request.json()
    prompt = data.get("query", "")
    response = query_granite(prompt)
    return JSONResponse({"response": response})

@app.post("/report")
async def report_ai(request: Request):
    data = await request.json()
    prompt = "Generate a sustainability report about: " + data.get("query", "")
    response = query_granite(prompt)
    return JSONResponse({"response": response})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
