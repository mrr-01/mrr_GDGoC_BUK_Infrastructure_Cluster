from fastapi import FastAPI

app = FastAPI(title="CampusBoard API")

@app.get("/")
def root():
    return {"message": "CampusBoard API is running", "status": "healthy"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
