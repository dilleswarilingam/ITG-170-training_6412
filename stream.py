from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.post("/upload-stream")
async def upload_stream(file: UploadFile = File(...)):

    
    async def generator_file():
        while True:
            chunk = await file.read(1024)  # read 1KB at a time
            if not chunk:
                break
            yield chunk

    return StreamingResponse(generator_file(), media_type="text/plain")
