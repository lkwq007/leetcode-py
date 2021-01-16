class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # sliding windows
        record={}
        start=0
        ret=0
        for i,item in enumerate(tree,0):
            if item not in record and len(record)==2:
                last=tree[i-1]
                for k in list(record.keys()):
                    if k!=last:
                        idx=record[k]
                        start=idx+1
                        del record[k]
            record[item]=i
            ret=max(ret,i-start+1)
        return ret
