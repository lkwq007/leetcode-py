class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block=False
        ret=[]
        row=[]
        for line in source:
            idx=0
            total=len(line)
            while idx<total:
                if block and line[idx]=="*" and idx+1<total and line[idx+1]=="/":
                    block=False
                    idx+=1
                elif not block and line[idx]=="/" and idx+1<total:
                    if line[idx+1]=="*":
                        block=True
                        idx+=1
                    elif line[idx+1]=="/":
                        break
                    else:
                        row.append(line[idx])
                elif not block:
                    row.append(line[idx])
                idx+=1
            if not block and row:
                ret.append("".join(row))
                row=[]
        return ret