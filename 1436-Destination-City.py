class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        record={}
        for src,dst in paths:
            if dst not in record:
                record[dst]=0
            if src in record:
                record[src]+=1
            else:
                record[src]=1
        for key,val in record.items():
            if val==0:
                return key