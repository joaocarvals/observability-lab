from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Observability Lab API",
    description="API para estudos de SRE e Observabilidade",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "online",
        "service": "observability-api",
        "timestamp": datetime.now()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }