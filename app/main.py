from fastapi import FastAPI
from datetime import datetime
from app.logger import logger


app = FastAPI(
    title="Observability Lab API",
    description="API para estudos de SRE e Observabilidade",
    version="1.0.0"
)


@app.get("/")
def home():

    logger.info("Endpoint principal acessado")

    return {
        "status": "online",
        "service": "observability-api",
        "timestamp": datetime.now()
    }


@app.get("/health")
def health_check():

    logger.info("Health check executado")

    return {
        "status": "healthy"
    }