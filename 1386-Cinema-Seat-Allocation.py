class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        occupied=0
        left_set=set([2,3,4,5])
        right_set=set([6,7,8,9])
        middle_set=set([4,5,6,7])
        left=0
        right=0
        middle=0
        cur=0
        idx=0
        ret=0
        while idx<len(reservedSeats):
            item=reservedSeats[idx]
            if cur!=item[0]:
                ret+=left+right if left+right>0 else middle
                left=1
                right=1
                middle=1
                cur=item[0]
                occupied+=1
            if item[1] in left_set:
                left=0
            if item[1] in right_set:
                right=0
            if item[1] in middle_set:
                middle=0
            idx+=1
        ret+=left+right if left+right>0 else middle
        return ret+2*(n-occupied)
