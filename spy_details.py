from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy()

#friend_one = Spy('akshit', 'Mr.', 5.5, 21)
#friend_two = Spy('arpit', 'Ms.', 4.4, 21)
#friend_three = Spy('Mohit', 'Mr.', 4.95, 20)


friends = []