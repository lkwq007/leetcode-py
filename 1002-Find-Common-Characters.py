class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        record=[0]*26
        template=record[:]
        base=ord("a")
        for item in A[0]:
            record[ord(item)-base]+=1
        for word in A[1:]:
            tmp=template[:]
            for item in word:
                idx=ord(item)-base
                tmp[idx]+=1
            for i in range(26):
                record[i]=min(record[i],tmp[i])
        ret=""
        for i in range(26):
            ret+=chr(base+i)*record[i]
        return list(ret)
