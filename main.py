from fastapi import FastAPI
from api.routes import books

app = FastAPI()
app.include_router(books.router)