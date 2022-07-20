class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        record={}
        def convert(x):
            acc=0
            while x>0:
                acc+=(x%10)
                x=x//10
            return acc
        for item in nums:
            cur=convert(item)
            if cur not in record:
                record[cur]=[]
            record[cur].append(item)
        ret=-1
        for _,v in record.items():
            if len(v)>1:
                v.sort()
                ret=max(ret,v[-1]+v[-2])
        return ret

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        record={}
        def convert(x):
            acc=0
            while x>0:
                acc+=(x%10)
                x=x//10
            return acc
        ret=-1
        for item in nums:
            cur=convert(item)
            if cur not in record:
                record[cur]=item
            else:
                ret=max(ret,record[cur]+item)
                record[cur]=max(record[cur],item)
        return ret