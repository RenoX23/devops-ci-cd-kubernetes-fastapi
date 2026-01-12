from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="DevOps Demo App")

@app.get("/", response_class=PlainTextResponse)
def root():
    return "FastAPI app is running"

@app.get("/health", response_class=PlainTextResponse)
def health():
    return "OK"
