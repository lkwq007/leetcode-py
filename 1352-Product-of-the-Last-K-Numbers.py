class ProductOfNumbers:

    def __init__(self):
        # At any time, the product of any contiguous sequence of numbers will 
        # fit into a single 32-bit integer without overflowing.
        self.array=[1]
        self.total=0

    def add(self, num: int) -> None:
        if self.array[-1]==0:
            self.array.append(num)
        else:
            self.array.append(num*self.array[-1])
        # self.total+=1

    def getProduct(self, k: int) -> int:
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)