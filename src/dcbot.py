import wrbcommands
import discord
import asyncio

loop = asyncio.get_event_loop()

BOTS = {}

class Dcbot(discord.Client):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.channel = None

    async def on_message(self, message):
        print(message.content)
        print(message.author)
        print(message.channel)
        print(self.user)
        if message.author != self.user:
            self.channel = message.channel
            wrbcommands.handle(message.author, message.content, self)

    def send(self, message):
        print(message)
        loop.create_task(self.channel.send(message))

    def sendImage(self, image_url, message=''):
        self.send(message + image_url)

    def begin(self):
        self.run(self.token)

def addBot(token):
    BOTS[token] = Dcbot(token)
    BOTS[token].begin()
        
if __name__ == '__main__':
    TOKEN = 'NDk2ODg0OTgwNDkyNzk1OTE5.W7Q2Mw.3kQCztzlOdv9gO_efZO56ezsW04'
    addBot(TOKEN)
        
# vim: sts=4 sw=4 ts=4 expandtab ft=python
