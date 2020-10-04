class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # two pass
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        ret=0
        if k==0:
            for _,val in record.items():
                if val>1:
                    ret+=1
        else:
            for key,_ in record.items():
                if key-k in record:
                    ret+=1
        return ret