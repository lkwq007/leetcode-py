class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        # brute force
        lst=[(-item,i) for i,item in enumerate(height)]
        lst.sort()
        left=lst[0][1]
        right=left
        ret=0
        for item,idx in lst:
            val=-item
            if left<=idx<=right:
                continue
            while left>idx:
                left-=1
                if left!=idx:
                    ret+=val-height[left]
            while right<idx:
                right+=1
                if right!=idx:
                    ret+=val-height[right]
        return ret

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        left=[0]*len(height)
        right=[0]*len(height)
        acc=0
        for i in range(len(height)):
            left[i]=acc
            acc=max(height[i],acc)
        acc=0
        for i in range(len(height)-1,-1,-1):
            right[i]=acc
            acc=max(height[i],acc)
        ret=0
        # print(left,right)
        for i in range(len(height)):
            ret+=max(0,min(left[i],right[i])-height[i])
        return ret