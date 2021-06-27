class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # the num range is limited
        ret=[]
        count=[0]*20002
        total=20001
        def bit_sum(pos):
            acc=0
            while pos>=0:
                acc+=count[pos]
                pos=((pos+1)&pos)-1
            return acc
        def update(pos):
            while pos<total:
                count[pos]+=1
                pos=(pos+1)|pos
        for i in range(len(nums)-1,-1,-1):
            item=nums[i]
            ret.append(bit_sum(item+10000-1))
            update(item+10000)
        return ret[::-1]