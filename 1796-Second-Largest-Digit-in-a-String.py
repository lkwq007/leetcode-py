class Solution:
    def secondHighest(self, s: str) -> int:
        first,second=-1,-1
        for item in s:
            if item.isdigit():
                val=int(item)
                if val>first:
                    second=first
                    first=val
                elif val>second and val!=first:
                    second=val
        return second