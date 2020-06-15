class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx=0
        total=len(bits)
        while idx<total:
            if bits[idx]==0:
                if idx==total-1:
                    return True
                idx+=1
            else:
                idx+=2
        return False