class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping={}
        idx=len(nums2)-1
        stack=[]
        ret=[-1]*len(nums1)
        while idx>=0:
            item=nums2[idx]
            while stack:
                if item<stack[-1]:
                    break
                else:
                    stack.pop()
            if stack:
                mapping[item]=stack[-1]
            else:
                mapping[item]=-1
            stack.append(item)
            idx-=1
        for idx in range(0,len(nums1)):
            ret[idx]=mapping[nums1[idx]]
        return ret