class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        idx0=0
        idx1=0
        carry=0
        while idx0<len(start) and idx1<len(end):
            if start[idx0]==end[idx1]:
                idx0+=1
                idx1+=1
            else:
                cur=start[idx0]+end[idx1]
                if cur=="RX":
                    carry+=1
                    idx1+=1
                elif cur=="XR":
                    carry-=1
                    idx0+=1
                elif cur=="LX":
                    
                elif cur=="XL":
                    pass
                else:
                    return False
        return True