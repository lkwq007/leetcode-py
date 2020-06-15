class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cur=""
        last=0
        cnt=0
        total=0
        for item in s:
            if item!=last:
                