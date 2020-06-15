from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length=len(s)
        if length<2:
            return s
        middle_plus_1=length//2
        idx=0
        while idx<middle_plus_1:
            s[idx],s[length-idx-1]=s[length-idx-1],s[idx]
            idx+=1
        return s
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    length=len(s)
    if length<2:
        return s
    middle_plus_1=length//2
    idx=0
    while idx<middle_plus_1:
        s[idx],s[length-idx-1]=s[length-idx-1],s[idx]
        idx+=1
    return s
print(reverseString("a b".split()))
print(reverseString("a b c".split()))
print(reverseString("a b c d".split()))
