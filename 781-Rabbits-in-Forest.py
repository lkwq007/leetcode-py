class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        record={}
        for item in answers:
            record[item]=record.get(item,0)+1
        ret=0
        for k,v in record.items():
            term=k+1
            cnt=v//term
            if v%term!=0:
                cnt+=1
            ret+=cnt*term
        return ret