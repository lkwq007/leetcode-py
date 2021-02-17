class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        acc=0
        # non-decreasing
        acc+=customers[0][1]
        cur=sum(customers[0])
        for i in range(1,len(customers)):
            cur=max(cur,customers[i][0])
            cur+=customers[i][1]
            acc+=cur-customers[i][0]
        return acc/len(customers)