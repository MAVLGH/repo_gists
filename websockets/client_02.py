import datetime
import asyncio
import websockets
from concurrent.futures import ThreadPoolExecutor

async def send_function(host, port, message):
    async with websockets.connect(f'ws://{host}:{port}') as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received: {response}")

def threaded_send(host, port, message):
    loop = asyncio.get_event_loop()
    asyncio.run_coroutine_threadsafe(send_function(host, port, message), loop)

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8765

    # Start event loop in main thread
    loop = asyncio.get_event_loop()

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        for i in range(10):
            message = f"Hello {i} at {datetime.datetime.utcnow()}"
            executor.submit(threaded_send, HOST, PORT, message)

    # Keep running the event loop
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
