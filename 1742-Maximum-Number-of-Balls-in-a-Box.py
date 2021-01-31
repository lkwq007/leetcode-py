class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        record={}
        for i in range(lowLimit,highLimit+1):
            acc=0
            while i>0:
                acc+=(i%10)
                i=i//10
            record[acc]=record.get(acc,0)+1
        return max(record.values())

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        record=[0]*50
        for i in range(lowLimit,highLimit+1):
            acc=0
            while i>0:
                acc+=(i%10)
                i=i//10
            record[acc]+=1
        return max(record)