class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ret=[0]*len(nums)
        record={}
        for i in range(len(nums)):
            item=nums[i]
            if item not in record:
                record[item]=[]
            record[item].append(i)
        for k,v in record.items():
            lst=v
            total=len(lst)
            acc=sum(lst)-total*lst[0]
            ret[lst[0]]=acc
            for i in range(1,total):
                diff=lst[i]-lst[i-1]
                acc=acc+(i-1)*diff-(total-i-1)*diff
                ret[lst[i]]=acc
        return ret
