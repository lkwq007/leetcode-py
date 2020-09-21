class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        mapping=[0]*201
        for i in range(len(products)):
            mapping[products[i]]=i
        self.mapping=mapping
        self.prices=prices
        self.discount=discount
        self.n=n
        self.cnt=0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total=0
        for id,num in zip(product,amount):
            total+=self.prices[self.mapping[id]]*num
        self.cnt+=1
        if self.cnt==self.n:
            total=total-self.discount*total/100.0
            self.cnt=0
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)