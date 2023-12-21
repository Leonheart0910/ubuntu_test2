from fastapi import FastAPI, Request

app = FastAPI()

# 퀴즈 페이지 결과를 처리하는 엔드포인트
cnt = 0

@app.get("/get_cnt")
async def get_cnt():
    return {"cnt": cnt}
@app.post("/update_cnt/{increment}")
async def update_cnt(increment: int):
    global cnt
    cnt += increment
    print(f"Current cnt value: {cnt}")
    return {"cnt": cnt}
@app.post("/reset_cnt")
async def reset_cnt():
    global cnt
    cnt = 0
    return {"cnt": cnt}

from fastapi.responses import FileResponse

@app.get("/")
async def root():
    return FileResponse('index.html')
