import uvicorn
from datetime import datetime
from fastapi import FastAPI
from starlette.responses import FileResponse
from public.router_users import user_router

app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
def on_startup():
    open("log_p.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')


@app.on_event("shutdown")
def shutdown():
    open("log_p.txt", mode="a").write(f'{datetime.utcnow()}: End\n')


@app.get("/")
def main():
    return FileResponse("index.html")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
