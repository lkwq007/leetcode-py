class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ret=[]
        lst=[0]*n
        acc=0
        for i in range(len(queries)):
            idx,color=queries[i]
            left,right=0,0
            if lst[idx]!=color:
                if idx>0:
                    if lst[idx-1]==lst[idx] and lst[idx]>0:
                        left-=1
                    if lst[idx-1]==color:
                        left+=1
                if idx+1<n:
                    if lst[idx+1]==lst[idx] and lst[idx]>0:
                        right-=1
                    if lst[idx+1]==color:
                        right+=1
                acc+=left+right
            lst[idx]=color
            ret.append(acc)
        return ret