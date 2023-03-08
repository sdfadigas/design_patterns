class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)
            
class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.notify_rat = Event()
    
    def action_rat_enters(self, rat):
        self.rat_enters(rat)

    def action_notify_rat(self, rat):
        self.notify_rat(rat)
        
class Rat:
    def __init__(self, game: Game):
        self.game = game
        self.game.rat_enters.append(self.rat_enters)
        self.game.notify_rat.append(self.notify_rat)
        self.attack: int = 1

    def rat_enters(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(self)

    def notify_rat(self, which_rat):
        if which_rat == self:
            return
        self.attack += 1

def test_single_rat():
    game = Game()
    rat = Rat(game)
    assert rat.attack == 1
    game.action_rat_enters(rat)
    assert rat.attack == 1
    print(f"rat 1: {rat.attack} should equal 1.")


def test_two_rats():
    game = Game()
    rat = Rat(game)
    rat2 = Rat(game)
    assert rat.attack == 1
    assert rat2.attack == 1
    game.action_rat_enters(rat)
    assert rat.attack == 2
    assert rat2.attack == 2
    game.action_rat_enters(rat2)
    assert rat.attack == 2
    assert rat2.attack == 2
    print(f"rat 1: {rat.attack} should equal 2.")
    print(f"rat 2: {rat2.attack} should equal 2.")


test_single_rat()
print("\n")
test_two_rats()