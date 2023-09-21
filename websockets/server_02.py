import asyncio
import websockets

class WebSocketServer:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.verbose = 0

    async def handler(self, websocket):
        await self.on_open()
        try:
            async for message in websocket:
                await self.on_message(message)
                response = f"Echo: {message}"
                await websocket.send(response)
        except:
            pass
        finally:
            await self.on_close()

    async def on_open(self):
        print("WebSocket opened") if self.verbose > 1 else None

    async def on_message(self, message):
        print(f"Received: {message}") if self.verbose > 0 else None

    async def on_close(self):
        print("WebSocket closed") if self.verbose > 1 else None

    def run(self, verbose):
        self.verbose=verbose
        server = websockets.serve(self.handler, self.host, self.port)
        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 8765
    server = WebSocketServer(host=HOST, port=PORT)
    server.run(verbose=1)
