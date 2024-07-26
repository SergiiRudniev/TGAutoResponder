import asyncio
import AI
import config
from pyrogram import enums

class Bot:
    def __init__(self, app):
        self.app = app
        self.InteractedUsers = set()
        self.FullInteractedUsers = set()
        self.Ai = AI.AI()

    async def SendMessageAudio(self, message):
        await self.app.send_message(message.chat.id, config.first_text)
        await self.app.send_audio(message.chat.id, "music.mp3")

    async def SendDisappearingMessage(self, message, text):
        msg = await self.app.send_message(message.chat.id, text)
        await asyncio.sleep(2)
        await msg.delete()
        await message.delete()

    async def OnMessage(self, message):
        if message.chat.id not in self.InteractedUsers and message.chat.id not in self.FullInteractedUsers:
            self.InteractedUsers.add(message.chat.id)
            await self.SendMessageAudio(message)
            await self.app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
            await self.app.send_message(message.chat.id, await self.Ai.CreateMessage(message.chat.id, message.text))

        elif message.chat.id in self.InteractedUsers and message.chat.id not in self.FullInteractedUsers:
            await self.app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
            await self.app.send_message(message.chat.id,
                                        await self.Ai.CreateMessage(message.chat.id, message.text))

    async def Cls(self, message):
        self.InteractedUsers.clear()
        self.FullInteractedUsers.clear()
        await self.SendDisappearingMessage(message, "Очистка успешна!!")

    async def Stop(self, message):
        self.FullInteractedUsers.add(message.chat.id)
        self.InteractedUsers.add(message.chat.id)
        await self.SendDisappearingMessage(message, "Успешно!")
