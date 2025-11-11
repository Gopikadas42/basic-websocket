import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("chat",self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat")

    async def receive(self,text_data):
        data=json.load(text_data)
        message=data['message']
        await self.channel_layer.group_send(
            "chat",
            {
                "type":"chat_message",
                "message":message
            }
        )
    async def chat_message(self,event):
        message=event['message']
        await self.send(text_data=json.dumps({
            "message": message
        } ))





