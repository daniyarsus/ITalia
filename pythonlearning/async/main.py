import asyncio

async def say_hello(name):
    try:
        await asyncio.sleep(2)
        print(f"hello, {name}")
    except Exception as e:
        print(f"an error: {e}")


async def main():
    await say_hello("Alice")
    await say_hello("Bob")
    await say_hello("Jo")

asyncio.run(main())