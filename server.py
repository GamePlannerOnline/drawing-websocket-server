import asyncio
import websockets
import logging

# create handler for each connection

PORT = 8000
HOST = "0.0.0.0"

async def handler(websocket: websockets.WebSocketServerProtocol, path):
    data = await websocket.recv()
    reply = f"Data recieved as: {data}!"
    await websocket.send(reply)

start_server = websockets.serve(handler, HOST, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

logging.info(f"Server started at ws://{HOST}:{PORT}")

