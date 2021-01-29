class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # brute force
        record={}
        ret={}
        for item in A:
            target={}
            target[item]=1
            ret[item]=1
            for key in record.keys():
                target[item|key]=1
                ret[item|key]=1
            record=target
        return len(ret)