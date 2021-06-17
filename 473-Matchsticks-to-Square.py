class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%4!=0:
            return False
        edge=total//4
        nums.sort(key=lambda x:-x)
        self.flag=False
        def probe(idx,tup):
            if idx>=len(nums):
                return all(map(lambda x:x==edge,tup))
            # tup is sorted
            cur=set([])
            for i in range(4):
                lst=list(tup)
                lst[i]+=nums[idx]
                if lst[i]>edge:
                    continue
                lst.sort()
                cur.add(tuple(lst))
            for item in cur:
                if probe(idx+1,item):
                    return True
            return False
        return probe(0,(0,)*4)
