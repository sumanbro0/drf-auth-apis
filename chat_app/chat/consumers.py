import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket connection closed with code: {close_code}")
        await self.close()

    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({
            'message': text_data
        }))
