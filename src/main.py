import fastapi
from src.orders.router import router

app = fastapi.FastAPI()
app.include_router(router)
