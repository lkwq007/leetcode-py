class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # brute force
        record=[i for i in range(m+1)]
        record_r=[i for i in range(m+1)]
        ret=[]
        for q in queries:
            val=record[q]
            ret.append(val-1)
            record[q]=1
            while val>1:
                record_r[val]=record_r[val-1]
                item=record_r[val]
                record[item]=val
                val-=1
            record_r[1]=q
        return ret