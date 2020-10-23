class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        ret=2
        record={nums[0]:1}
        meta_record={1:1}
        for i in range(1,len(nums)):
            item=nums[i]
            record[item]=record.get(item,0)+1
            meta_record[record[item]]=meta_record.get(record[item],0)+1
            if record[item]!=1:
                if meta_record[record[item]-1]==1:
                    del meta_record[record[item]-1]
                else:
                    meta_record[record[item]-1]-=1
            if len(meta_record)==1 and i!=len(nums)-1:
                ret=max(ret,i+2)
            if len(meta_record)==2:
                keys=sorted(meta_record.keys())
                if meta_record.get(1,0)==1:
                    ret=max(ret,i+1)
                elif keys[1]==keys[0]+1 and meta_record[keys[1]]==1:
                    ret=max(ret,i+1)
        return ret