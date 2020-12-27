class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, to_withdraw):
        if to_withdraw > self.balance:
            raise ValueError
        self.balance -= to_withdraw
        return f"{self.name} has {self.balance}."

    def add_cash(self, to_add):
        self.balance += to_add
        return f"{self.name} has {self.balance}."

    def check(self, second_person, transfer_sum):
        if (not second_person.checking_account) or transfer_sum > second_person.balance:
            raise ValueError
        self.balance += transfer_sum
        second_person.balance -= transfer_sum

        return f"{self.name} has {self.balance} and {second_person.name} has {second_person.balance}."


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

Jeff.withdraw(2)
Joe.check(Jeff, 50)
Jeff.check(Joe, 80)
Jeff.add_cash(20)
