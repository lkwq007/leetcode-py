class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lst=text.split()
        ret=[]
        idx=0
        total=len(lst)-1
        while idx<total:
            if lst[idx]==first and lst[idx+1]==second and idx+2<=total:
                ret.append(lst[idx+2])
            idx+=1
        return ret