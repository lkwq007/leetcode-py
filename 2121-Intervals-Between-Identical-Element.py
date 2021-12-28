class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        record={}
        ret=[0]*len(arr)
        for i in range(len(arr)):
            item=arr[i]
            if item not in record:
                record[item]=[]
            record[item].append(i)
            ret[record[item][0]]+=i-record[item][0]
        for k,v in record.items():
            for i in range(1,len(v)):
                idx=v[i]
                prev=v[i-1]
                diff=(idx-prev)*(i+i-len(v))
                ret[idx]=ret[prev]+diff
        return ret