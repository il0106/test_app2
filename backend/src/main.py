from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 
from config import settings
from users.router import router as router_users


app = FastAPI()
app.include_router(router_users)

# Разрешаем CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS.split(','),  # В продакшене укажите конкретный домен фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sum")
def read_sum(a: float, b: float):
    return {"sum": a + b}


@app.get("/settings")
def read_config():
    return {str(settings)}




if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.BACKEND_PORT, reload=True) # здесь важно именно 0.0.0.0