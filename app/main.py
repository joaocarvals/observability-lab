from fastapi import FastAPI
from datetime import datetime
from app.logger import logger
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(
    title="Observability Lab API",
    description="API para estudos de SRE e Observabilidade",
    version="1.0.0"
)

Instrumentator().instrument(app).expose(app)

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