class ATM:

    def __init__(self):
        self.cnt=[0]*5
        self.val=[20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.cnt[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ret=[0]*5
        acc=amount
        for i in range(len(self.cnt)-1,-1,-1):
            if self.cnt[i]>0 and acc>=self.val[i]:
                cnt=min(self.cnt[i],acc//self.val[i])
                acc-=cnt*self.val[i]
                ret[i]=cnt
        if acc==0:
            for i in range(5):
                self.cnt[i]-=ret[i]
            return ret
        else:
            return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)