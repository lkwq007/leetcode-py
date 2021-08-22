class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        record={}
        for num in nums:
            acc=0
            for item in num:
                acc=acc<<1
                acc+=int(item)
            record[acc]=1
        for i in range(17):
            if i not in record:
                ret=["0"]*len(nums)
                pos=-1
                while i>0:
                    if i&1:
                        ret[pos]="1"
                    pos-=1
                    i=i>>1
                return "".join(ret)
