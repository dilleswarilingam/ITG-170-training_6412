from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time 

app=FastAPI()

def generate_data():
    for i in range(1,6):
        yield f"data:{i}"
        time.sleep(1)

@app.get("/stream")
def streaming():
    return StreamingResponse(generate_data())
