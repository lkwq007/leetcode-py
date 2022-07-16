class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        base=ord("a")
        mapping={}
        cnt=0
        for i in range(len(key)):
            if key[i]!=" " and key[i] not in mapping:
                mapping[key[i]]=chr(base+cnt)
                cnt+=1
        ret=""
        mapping[" "]=" "
        for item in message:
            ret+=mapping[item]
        return ret
