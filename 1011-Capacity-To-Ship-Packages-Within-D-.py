class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(x):
            ret=1
            cur=x
            for item in weights:
                if item>cur:
                    ret+=1
                    cur=x-item
                else:
                    cur-=item
            return ret<=days
        left=max(weights)
        right=sum(weights)
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                right=middle
            else:
                left=middle+1
        return left
        