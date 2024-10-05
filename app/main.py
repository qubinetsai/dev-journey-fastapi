from fastapi import FastAPI
from app.routes.user import router as user_router
from app.utils.auth import engine
from app.models.user import Base

app = FastAPI()

# Include your routers
app.include_router(user_router)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return "Welcome to the FastAPI Hello World Project!"

