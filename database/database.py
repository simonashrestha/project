from sqlalchemy import Column, Integer, MetaData, String, Table, Text, create_engine
from databases import Database

DATABASE_URL = "sqlite:///./database.db"
database = Database(DATABASE_URL)
metadata = MetaData()

blogs = Table(
    "blogs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("blog_description", Text),
    Column("self_description", Text),
    Column("gender", String),
)

# Create the table in the database
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
