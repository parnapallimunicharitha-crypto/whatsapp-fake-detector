from fastapi import FastAPI
from routes.whatsapp import router as whatsapp_router

app = FastAPI()

app.include_router(whatsapp_router)

@app.get("/")
def home():
    return {
        "status": "running 🚀",
        "message": "WhatsApp Fake Detector API is live",
        "docs": "/docs"
    }


# from fastapi import FastAPI
# from routes.whatsapp import router as whatsapp_router

# app = FastAPI()

# app.include_router(whatsapp_router)

# @app.get("/")
# def home():
#     return {"status": "Bot is running 🚀"}