import datetime
import asyncio
import websockets

async def send_function(host, port):
    async with websockets.connect(f'ws://{host}:{port}') as websocket:
        await websocket.send(f"Hello at {datetime.datetime.utcnow()}")
        response = await websocket.recv()
        print(f"Received: {response}")

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8765
    asyncio.get_event_loop().run_until_complete(send_function(host=HOST, port=PORT))
