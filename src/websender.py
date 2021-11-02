import asyncio
import json
import websockets
import JSON_Contractor

# https://github.com/ParametricCamp/TutorialFiles/blob/master/Misc/WebSockets/python-websockets/client.py

PORT = JSON_Contractor.LoadConfig()["SOCKET_PORT"]
ADDR = JSON_Contractor.LoadConfig()["SOCKET_IP"]

async def send_json(book):
    json_string = json.dumps(book)
    async with websockets.connect("ws://" + ADDR + ":" + PORT) as websocket:
        await websocket.send(str(json_string))

#
# bok = {
#     "prg": 1.0
# }
#
# asyncio.get_event_loop().run_until_complete(send_json(bok))
