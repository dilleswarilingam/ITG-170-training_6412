from fastapi import FastAPI,Request
import time
app=FastAPI()

@app.middleware("http")
async def login_time (request: Request,call_next):
    process_time=time.perf_counter()
    response=await call_next(request)
    status_time=time.perf_counter()-process_time
    response.headers["x-status_time"]=str(status_time)
    return response

@app.get("/")
def get_time():
    return 