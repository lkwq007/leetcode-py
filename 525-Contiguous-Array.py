class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        acc=0
        mapping={0:-1}
        max_len=0
        for idx in range(0,len(nums)):
            item=nums[idx]
            if item>0:
                acc+=1
            else:
                acc-=1
            if acc in mapping:
                max_len=max(max_len,idx-mapping[acc])
            else:
                mapping[acc]=idx
        return max_len
        

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        total=0
        for item in nums:
            total+=item
        self.max=0
        def check(start,end,total):
            if 2*total==end-start+1:
                self.max=max(self.max,end-start+1)
                return
            if 2*total>(end-start+1):
                
        while 2*total!=(end-start+1) and end>=start:
            if 2*total>(end-start+1):
                if nums[start]:
                    start+=1
                    total-=1
                elif nums[end]:
                    end-=1
                    total-=1
                else:
                    start+=1
            else:
                if nums[start]==0:
                    start+=1
                elif nums[end]==0:
                    end-=1
                else:
                    start+=1
                    total-=1
        if end<start:
            return 0
        else:
            return end-start+1