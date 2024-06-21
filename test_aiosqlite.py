import aiosqlite
import asyncio

async def test():
    async with aiosqlite.connect('test.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
        await db.execute('INSERT INTO test (name) VALUES (?)', ('Alice',))
        await db.commit()
        async with db.execute('SELECT * FROM test') as cursor:
            async for row in cursor:
                print(row)

asyncio.run(test())
