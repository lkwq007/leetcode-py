class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban=set(banned)
        acc=maxSum
        ret=0
        for i in range(1,n+1):
            if i>acc:
                break
            if i not in ban:
                ret+=1
                acc-=i
        return ret
