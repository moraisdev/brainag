from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.routes import producer, dashboard

app = FastAPI(
    title="Farm Producer Management API",
    version="1.0.0",
    description="API to manage farm producers and provide analytics for a dashboard.",
)

app.include_router(producer.router, prefix="/producers", tags=["Producers"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "OK"}
