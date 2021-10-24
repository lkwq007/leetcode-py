class Bank:

    def __init__(self, balance: List[int]):
        self.total=len(balance)
        self.balance=balance[:]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0<account1<=self.total and 0<account2<=self.total and self.balance[account1-1]>=money:
            self.balance[account1-1]-=money
            self.balance[account2-1]+=money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0<account<=self.total:
            self.balance[account-1]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0<account<=self.total and self.balance[account-1]>=money:
            self.balance[account-1]-=money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)