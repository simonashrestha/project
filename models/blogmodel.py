from sqlalchemy import select
from models import database, blogs

async def create_blog(blog_description, self_description, gender):
    query= blogs.insert().values(
        blog_description=blog_description,
        self_description= self_description,
        gender= gender,
    )
    return await database.execute(query)

async def get_blog(id):
    query = select(blogs).where(blogs.c.id == id)
    # logger.debug(f"Executing query: {query}")
    result = await database.fetch_one(query)
    # logger.debug(f"Query result: {result}")
    return result


# async def update_blog(username):
#     query= blogs.update().where(blogs.c.username==username)
#     return await database.execute(query)

async def update_blog(id, data):
    query = (
        blogs.update()
        .where(blogs.c.id == id)
        .values(
        
            blog_description=data.get("blog_description"),
            self_description=data.get("self_description"),
            gender=data.get("gender"),
        
        )
    )
    await database.execute(query)

async def delete_blog(id):
    query = blogs.delete().where(blogs.c.id == id)
    return await database.execute(query)


