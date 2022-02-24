class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        even={}
        odd={}
        for i in range(0,len(nums),2):
            item=nums[i]
            even[item]=even.get(item,0)+1
        for i in range(1,len(nums),2):
            item=nums[i]
            odd[item]=odd.get(item,0)+1
        cnt0=len(nums)//2
        cnt1=(len(nums)+1)//2
        key0=list(even.keys())
        key1=list(odd.keys())
        key0.sort(key=lambda x:-even[x])
        key1.sort(key=lambda x:-odd[x])
        first0=key0[0]
        first1=key1[0]
        if first0!=first1:
            return cnt0-even[first0]+cnt1-odd[first1]
        second0=key0[1] if len(key0)>1 else first0-1
        second1=key1[1] if len(key1)>1 else first1-1
        return min(len(nums)-even[first0]-odd.get(second1,0),len(nums)-even.get(second0,0)-odd[first1])
        
