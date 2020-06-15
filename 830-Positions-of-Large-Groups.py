from typing import List

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        lst=list(S)
        ret=[]
        count=0
        cur=None
        for idx, item in enumerate(lst,0):
            if item!=cur:
                if count>2:
                    ret.append([idx-count,idx-1])
                count=1
                cur=item
            else:
                count+=1
        idx+=1
        if count>2:
            ret.append([idx-count,idx-1])
        return ret

def largeGroupPositions(S: str) -> List[List[int]]:
    lst=list(S)
    ret=[]
    count=0
    cur=None
    for idx, item in enumerate(lst,0):
        if item!=cur:
            if count>2:
                ret.append([idx-count,idx-1])
            count=1
            cur=item
        else:
            count+=1
    idx+=1
    if count>2:
        ret.append([idx-count,idx-1])
    return ret

print(largeGroupPositions("aaaaa"))