class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        acc=0
        for item in arr2:
            acc^=item
        ret=0
        for item in arr1:
            ret^=(item&acc)
        return ret

# xor 

# a&nb or na&b

# (a&b1)^(a&b2)

# (a&b1) & (na or nb2) or (na or nb1) & a &b2
# (a&b1&nb2) or (a & nb1 & b2)
# a & (b1^b2)