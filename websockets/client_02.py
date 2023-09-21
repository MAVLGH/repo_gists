import datetime
import asyncio
import websockets

async def send_function(host, port, message):
    async with websockets.connect(f'ws://{host}:{port}') as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received: {response}")

async def main():
    HOST = 'localhost'
    PORT = 8765
    tasks = []
    for i in range(100):
        message = f"Hello {i} at {datetime.datetime.utcnow()}"
        task = asyncio.ensure_future(send_function(HOST, PORT, message))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
