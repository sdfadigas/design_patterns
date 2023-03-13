from event import Event


class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.notify_rat = Event()            
        self.observers = []
        
    def add_rat(self, rat):
        self.observers.append(rat)
        rat.attack = len(self.observers)
        
    def remove_rat(self, rat):
        self.observers.remove(rat)  