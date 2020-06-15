class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs)<5:
            return -1
        template="croak"
        table={}
        record=[0]*5
        for idx,item in enumerate(template,0):
            table[item]=idx
        total=0
        for item in croakOfFrogs:
            if item in table:
                idx=table[item]
            else:
                return -1
            record[idx]+=1
            left=record[idx] if idx==0 else record[idx-1]
            if record[idx]>left:
                return -1
            total=max(max(record),total)
            if all(map(lambda x:x>0,record)):
                for i in range(5):
                    record[i]-=1
        if not all(map(lambda x:x==0,record)):
            return -1
        return total
