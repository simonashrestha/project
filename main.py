from routes import blogroutes
from starlette.applications import Starlette

app = Starlette(debug=True)
app.mount("/", blogroutes.app)

