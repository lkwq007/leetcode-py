class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def lowbound(x):
            left=max(x-index,0)
            right=max(x-(n-index-1),0)
            left_acc=(x+left)*(x-left+1)//2
            right_acc=(x+right)*(x-right+1)//2
            return left_acc+right_acc-x+n
        l=0
        r=maxSum
        while l<r:
            m=l+(r-l)//2
            tmp=lowbound(m)
            if tmp==maxSum:
                return m+1
            elif tmp>maxSum:
                r=m
            else:
                l=m+1
        return l if lowbound(l)>maxSum else l+1