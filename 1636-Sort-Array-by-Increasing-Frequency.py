class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:(record[x],-x))
        ret=[0]*len(nums)
        idx=0
        for key in keys:
            for i in range(record[key]):
                ret[idx]=key
                idx+=1
        return ret

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        record={}
        for item in nums:
            record[item]=record.get(item,0)+1
        return sorted(nums,key=lambda x:(record[x],-x))