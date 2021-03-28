class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        record={}
        for key,val in knowledge:
            record[key]=val
        ret=[]
        idx=0
        while idx<len(s):
            if s[idx]=="(":
                start=idx+1
                end=start
                while s[end]!=")":
                    end+=1
                idx=end+1
                ret.append(record.get(s[start:end],"?"))
            else:
                ret.append(s[idx])
                idx+=1
        return "".join(ret)