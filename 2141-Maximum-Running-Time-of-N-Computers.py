class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if n==1:
            return sum(batteries)
        if n==len(batteries):
            return min(batteries)
        total=sum(batteries)
        batteries.sort(key=lambda x:-x)
        def check(x):
            if x*n>total:
                return False
            l=0
            r=len(batteries)-1
            racc=batteries[-1]
            while l<n:
                acc=batteries[l]
                if acc>=x:
                    l+=1
                    continue
                while acc+racc<x:
                    r-=1
                    if r<n:
                        return False
                    acc+=racc
                    racc=batteries[r]
                racc=max(0,acc+racc-x)
                l+=1
            return True
        left=1
        right=total
        while left<right:
            middle=left+(right-left)//2
            # print(middle,check(middle))
            if check(middle):
                left=middle+1
            else:
                right=middle
        if check(left):
            return left
        return left-1

