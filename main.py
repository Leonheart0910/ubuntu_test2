from fastapi import FastAPI, Request

app = FastAPI()



@app.get("/")
async def root():
    return {"씨발 애미"}
