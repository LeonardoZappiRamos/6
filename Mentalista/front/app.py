from fastapi import FastAPI

app = FastAPI()


@app.get("/api/quiz")
async def get():
    return {"message": "Hello World"}
async def list(request):
    return {"message": "Hello World"}
  
@app.post("/api/quiz")
async def create(request):
  pass