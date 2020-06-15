class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hashtbl={}
        for item in J:
            hashtbl[item]=1
        ret=0
        for item in S:
            if item in hashtbl:
                ret+=1
        return ret