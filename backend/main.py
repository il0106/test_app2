from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 
# from src.users.router import router as router_users


app = FastAPI()
# app.include_router(router_users)

# Разрешаем CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:80",
        "http://109.196.102.43"],  # В продакшене укажите конкретный домен фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sum")
def read_sum(a: float, b: float):
    return {"sum": a + b}


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)