import functools
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # 1 <= nums.length <= 10^5
        # 1 <= nums[i] <= 10^5
        @functools.lru_cache(maxsize=None)
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        stack=[nums[0]]
        for i in range(1,len(nums)):
            item=nums[i]
            stack.append(item)
            while len(stack)>1:
                a,b=stack[-2],stack[-1]
                if a<b:
                    a,b=b,a
                cur=gcd(a,b)
                if cur>1:
                    val=stack.pop()
                    stack[-1]=stack[-1]*val//cur
                else:
                    break
        return stack

