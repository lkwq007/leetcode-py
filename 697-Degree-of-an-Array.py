class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_freq=1
        record={}
        lst=[]
        for i,item in enumerate(nums,0):
            if item not in record:
                record[item]=[0,i,i]
            record[item][0]+=1
            record[item][2]=i
            if record[item][0]>max_freq:
                lst=[item]
                max_freq=record[item][0]
            elif record[item][0]==max_freq:
                lst.append(item)
        ret=len(nums)
        for item in lst:
            ret=min(ret,record[item][2]-record[item][1]+1)
        return ret