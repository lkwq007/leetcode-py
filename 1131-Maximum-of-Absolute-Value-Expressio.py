class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # (a1_i-a1_j) + (a2_i-a2_j) + abs(i-j)
        # a1i+a2i-(a1j+a2j)
        # a1i-a2i-(a2j-a1j) 
        # a2i-a1i+(a1j-a2j)
        # -(a1i+a2i)+(a1j+a2j)
        a1_plus_a2=[a+b for a,b in zip(arr1,arr2)]
        a1_minus_a2=[a-b for a,b in zip(arr1,arr2)]

