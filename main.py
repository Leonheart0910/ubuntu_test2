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

@app.get("/Q1")
async def root():
    return FileResponse('Q1.html')

@app.get("/Q2")
async def root():
    return FileResponse('Q2.html')
@app.get("/Q3")
async def root():
    return FileResponse('Q3.html')
@app.get("/Q4")
async def root():
    return FileResponse('Q4.html')
@app.get("/Q5")
async def root():
    return FileResponse('Q5.html')

@app.get("/INFO")
async def root():
    return FileResponse('INFO.html')
@app.get("/RE1")
async def root():
    return FileResponse('RE1.html')
@app.get("/RE2")
async def root():
    return FileResponse('RE2.html')
@app.get("/RE3")
async def root():
    return FileResponse('RE3.html')
@app.get("/RE4")
async def root():
    return FileResponse('RE4.html')
@app.get("/RE5")
async def root():
    return FileResponse('RE5.html')

@app.get("/agree")
async def root():
    return FileResponse('agree.html')
@app.get("/insert")
async def root():
    return FileResponse('insert.html')
@app.get("/thanks")
async def root():
    return FileResponse('thanks.html')

# POST
from pydantic import BaseModel
class model(BaseModel):
    name: str
    phone: int

@app.post("/send")
def ppost (data : model):
    print(data)
    return {"전송완료"}