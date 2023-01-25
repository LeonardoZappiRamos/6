from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
  
@app.get("/admin")
async def root_admin():
  return {"message": "This is admin root"}