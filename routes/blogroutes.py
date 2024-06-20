
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from database.database import database
from starlette.routing import Route, Mount, Router
from models.blogmodel import create_blog, get_blog, update_blog, delete_blog
# from models import database, DATABASE_URL, metadata

# from crud import create_blog, get_blog, update_blog, delete_blog
from auth import authenticate_user

# app = Starlette(debug=True)
app= Router()

@app.route("/blogs/", methods=["POST"])
async def create(request: Request):
    data = await request.json()
    blog_description= data.get('blog_description')
    self_description= data.get('self_description')
    gender= data.get('gender')
    await create_blog(blog_description, self_description, gender)
    return JSONResponse({"message": "Blog created successfully"})

@app.route("/blogs/{id}/", methods=["GET"])
async def read(request: Request):
    username = request.path_params["id"]
    # print(username)
    blog = await get_blog(username)
    # print(blog)
    if blog:
        return JSONResponse(dict(blog))
    else:
        return JSONResponse({"message": "Blog not found"}, status_code=404)

# @app.route("/blogs/{username}/", methods=["PUT"])
# # @requires("authenticated")
# async def update(request: Request):
#     username = request.path_params["username"]
#     data = await request.json()
#     await update_blog(data)
#     return JSONResponse({"message": "Blog updated successfully"})

@app.route("/blogs/{id}/", methods=["PUT"])
# @requires("authenticated")
async def update(request: Request):
    id = request.path_params["id"]
    data = await request.json()
    await update_blog(id, data)
    return JSONResponse({"message": "Blog updated successfully"})

@app.route("/blogs/{id}/", methods=["DELETE"])
# @requires("authenticated")
async def delete(request: Request):
    id = request.path_params["id"]
    await delete_blog(id)
    return JSONResponse({"message": "Blog deleted successfully"})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000, reload=True)
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()