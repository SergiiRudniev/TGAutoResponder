import json
import g4f

class AI:
    def __init__(self):
        self._chat: dict[str, list] = {}

        with open("chat.json", "r") as file:
            self._chat = json.load(file)

    def DumpJson(self) -> None:

        with open("chat.json", "w") as file:
            json.dump(self._chat, file)

    async def CreateMessage(self, id: int, msg: str) -> str:
        try:
            self._chat[str(id)].append({"role": "user", "content": msg})
        except KeyError:
            self._chat[str(id)] = []
            self._chat[str(id)].append({"role": "user", "content": msg})
        responce = await g4f.ChatCompletion.create_async(model=g4f.models.gpt_35_turbo, messages=self._chat[str(id)])

        self._chat[str(id)].append({"role": "assistant", "content": responce})

        self.DumpJson()
        return responce

