class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        record={}
        if start==end:
            return 0
        for item in bank:
            record[item]=-1
        if end not in record:
            return -1
        queue=[start]
        step=0
        while queue:
            step+=1
            target=[]
            for item in queue:
                for i in range(len(item)-1):
                    for gene in ("A","C","G","T"):
                        next=item[:i]+gene+item[(i+1):]
                        if next==end:
                            return step
                        if next in record and record[next]==-1:
                            record[next]=step
                            target.append(next)
            queue=target
        return -1
