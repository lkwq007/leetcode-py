class Solution:
    def numDecodings(self, s: str) -> int:
        if s=="0":
            return 0
        first=0
        second=1
        # first second now
        last=0
        base=ord("0")
        for item in s:
            digit=ord(item)-base
            if digit==0 and (last<1 or last>2):
                # invalid encoding
                return 0
            if last==1 or (last==2 and digit<=6):
                if digit>0:
                    now=first+second
                else:
                    now=first
            elif digit>0:
                now=second
            else:
                now=0
            first=second
            second=now
            last=digit
        return now
