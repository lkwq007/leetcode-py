class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count(n):
            cnt=0
            tmp=n
            while n:
                cnt+=1
                n=n&(n-1)
            return cnt,tmp
        arr.sort(key=count)
        return arr