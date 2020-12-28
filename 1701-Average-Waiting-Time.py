class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        acc=0
        for arrival,time in customers:
            