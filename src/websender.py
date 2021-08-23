import asyncio
import json
import websockets


# https://github.com/ParametricCamp/TutorialFiles/blob/master/Misc/WebSockets/python-websockets/client.py

async def send_json(book):
    json_string = json.dumps(book)
    async with websockets.connect("ws://192.168.1.79:8765") as websocket:
        await websocket.send(str(json_string))

#
# bok = {
#     "prg": 1.0
# }
#
# asyncio.get_event_loop().run_until_complete(send_json(bok))
