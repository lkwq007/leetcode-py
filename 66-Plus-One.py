class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for idx in range(len(digits)-1,-1,-1):
            digits[idx]+=carry
            if digits[idx]>9:
                digits[idx]-=10
            else:
                return digits
        digits.insert(0,1)
        return digits
            