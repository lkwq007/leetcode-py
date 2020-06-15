class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # it is guaranteed that there exists at least one solution
        ret=[]
        record={}
        for idx in range(0,len(groupSizes)):
            size=groupSizes[idx]
            if size in record:
                record[size].append(idx)
            else:
                record[size]=[idx]
            if len(record[size])==size:
                ret.append(record[size])
                record[size]=[]
        return ret