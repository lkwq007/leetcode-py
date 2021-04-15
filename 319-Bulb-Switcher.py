class Solution:
    def bulbSwitch(self, n: int) -> int:
        # prime numbers are off
        if n==0:
            return 0
        return n//2