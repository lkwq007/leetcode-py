class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base=ord("a")-1
        def compute_key(str):
            lst=list(map(lambda x:ord(x)-base,str))
            lst.sort()
            acc=0
            for item in lst:
                acc*=100
                acc+=item
            return acc
        record=dict()
        for item in strs:
            key=compute_key(item)
            if key in record:
                record[key].append(item)
            else:
                record[key]=[item]
        return list(record.values())