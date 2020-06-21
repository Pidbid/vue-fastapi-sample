# -*-coding:utf-8-*-
from fastapi import FastAPI, UploadFile,File #Fastapi
from fastapi.middleware.cors import CORSMiddleware #跨域调用
import uvicorn 

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def recv_file(file: UploadFile = File(...)):
    file_data = await file.read()
    with open(file.filename,"wb") as fp:
        fp.write(file_data)
    fp.close()
    print(file.file)
    rt_msg = {
        "name": file.filename,
        "type": file.content_type
    }
    return rt_msg
