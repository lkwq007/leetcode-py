class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # DP
        dp=[0]*3
        for item in nums:
            for val in dp[:]:
                dp[(val+item)%3]=max(dp[(val+item)%3],val+item)
        return dp[0]


from collections import deque
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # using deque without sorting
        acc=0
        queue1=deque([],maxlen=2)
        queue2=deque([],maxlen=2)
        queue=[queue1,queue2]
        ret=0
        for item in nums:
            acc+=item
            if item%3!=0:
                idx=item%3-1
                if len(queue[idx])<1 or item<=queue[idx][-1]:
                    queue[idx].append(item)
                elif len(queue[idx])<2 and item>=queue[idx][0]:
                    queue[idx].appendleft(item)
                elif item<=queue[idx][0]:
                    queue[idx][0]=item
            if acc%3==0:
                ret=max(ret,acc)
            else:
                idx=acc%3-1
                if len(queue[idx])>0:
                    ret=max(ret,acc-min(queue[idx]))
                if len(queue[1-idx])>1:
                    ret=max(ret,acc-sum(queue[1-idx]))
        return ret

from collections import deque
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # using deque with sorting
        nums.sort(key=lambda x:-x)
        acc=0
        queue1=deque([],maxlen=2)
        queue2=deque([],maxlen=2)
        queue=[queue1,queue2]
        ret=0
        for item in nums:
            acc+=item
            if item%3!=0:
                idx=item%3-1
                queue[idx].append(item)
            if acc%3==0:
                ret=max(ret,acc)
            else:
                idx=acc%3-1
                if len(queue[idx])>0:
                    ret=max(ret,acc-min(queue[idx]))
                if len(queue[1-idx])>1:
                    ret=max(ret,acc-sum(queue[1-idx]))
        return ret

