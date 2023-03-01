from chat_room import *
class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.chat_room: ChatRoom = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message):
        self.chat_room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.chat_room.message(self.name, who, message)