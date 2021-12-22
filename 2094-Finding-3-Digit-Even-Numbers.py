class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # brute force
        ret=set([])
        for i in range(len(digits)):
            if digits[i]==0:
                continue
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if digits[k]%2==0 and i!=j and j!=k and i!=k:
                        ret.add(digits[i]*100+digits[j]*10+digits[k])
        return list(sorted(list(ret)))