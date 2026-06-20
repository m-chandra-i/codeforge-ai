from fastapi import FastAPI

app = FastAPI(
    title="CodeForge AI",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "CodeForge AI"
    }
