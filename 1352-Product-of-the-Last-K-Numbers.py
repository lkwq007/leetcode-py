class ProductOfNumbers:

    def __init__(self):
        # At any time, the product of any contiguous sequence of numbers will 
        # fit into a single 32-bit integer without overflowing.
        self.array=[1]
        self.total=0

    def add(self, num: int) -> None:
        # deal with zero case
        if num==0:
            self.array=[0,1]
        else:
            self.array.append(num*self.array[-1])
        self.total+=1

    def getProduct(self, k: int) -> int:
        if k>=len(self.array)-1 and self.array[0]==0:
            return 0
        return self.array[-1]//self.array[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)