class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        total=0
        acc=0
        for i in range(X):
            if grumpy[i]==0:
                total+=customers[i]
            else:
                acc+=customers[i]
        ret=acc
        for i in range(X,len(customers)):
            if grumpy[i]==0:
                total+=customers[i]
            else:
                acc+=customers[i]
                if grumpy[i-X]==1:
                    acc-=customers[i-X]
                ret=max(ret,acc)
        return total+ret