class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        a=sum(A)
        b=sum(B)
        diff=(a-b)//2
        record={}
        for item in B:
            record[item]=1
        for item in A:
            if item-diff in record:
                return [item,item-diff]
