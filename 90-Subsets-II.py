class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret=set([])
        def probe(idx,lst):
            if idx==len(nums):
                self.ret.add(tuple(lst))
                return
            probe(idx+1,lst)
            lst.append(nums[idx])
            probe(idx+1,lst)
            lst.pop()
        probe(0,[])
        return list(self.ret)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret=[]
        def probe(idx,lst):
            if idx==len(nums):
                self.ret.append(lst[:])
                return
            cnt=1
            lst.append(nums[idx])
            while idx+1<len(nums) and nums[idx+1]==nums[idx]:
                lst.append(nums[idx])
                idx+=1
                cnt+=1
            while cnt>0:
                probe(idx+1,lst)
                lst.pop()
                cnt-=1
            probe(idx+1,lst)
        probe(0,[])
        return self.ret