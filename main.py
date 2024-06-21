# from routes.blogroutes import app as blog_app
from starlette.applications import Starlette
from database.database import database

app = Starlette(debug=True)
# app.mount('/blogs', blog_app)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()