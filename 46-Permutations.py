class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n!
        record={}
        for item in nums:
            record[item]=1
        self.ret=[]
        total=len(nums)
        def perm(pos,lst):
            if pos==total:
                self.ret.append(lst[:])
                return
            keys=list(record.keys())
            for key in keys:
                cur=key
                lst[pos]=cur
                del record[key]
                perm(pos+1,lst)
                record[key]=1
        perm(0,nums)
        return self.ret