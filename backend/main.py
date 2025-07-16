import uvicorn
from config import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app", 
        host=settings["BACKEND_HOST"], 
        port=int(settings["BACKEND_PORT"]),
        log_level="info", 
        reload=settings["BACKEND_DEBUG"].lower() == "true"
    )