from routes import blogroutes
from starlette.applications import Starlette
from starlette.routing import Route, Mount, Router
app= Starlette()
app.mount(blogroutes.app)