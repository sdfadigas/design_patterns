from action import Action

class Command:
    def __init__(self, action: Action, amount: int):
        self.action = action
        self.amount = amount
        self.success = False

class DepositCommand(Command):
    def execute(self):
        self.account.balance += self.amount
        self.success = True

    def undo(self):
        self.account.balance -= self.amount


class WithdrawCommand(Command):
    def execute(self):
        if self.account.balance >= self.amount:
            self.account.balance -= self.amount
            self.success = True

    def undo(self):
        self.account.balance += self.amount