from fastapi import FastAPI
from .import database
from .import models
from .routers import user, blog, authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(database.engine)
