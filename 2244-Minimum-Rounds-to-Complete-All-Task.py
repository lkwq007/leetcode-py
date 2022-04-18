class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        record={}
        for item in tasks:
            record[item]=record.get(item,0)+1
        ret=0
        for k,v in record.items():
            if v<2:
                return -1
            elif v%3==0:
                ret+=v//3
            else:
                ret+=(v//3)+1
        return ret