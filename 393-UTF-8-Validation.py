class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        mask=0xff
        for i in range(len(data)):
            data[i]&=mask
        table=[(7,0),(5,6),(4,14),(3,30)]
        idx=0
        def match(item):
            for i in range(len(table)):
                if (item>>table[i][0])==table[i][1]:
                    return i
            return -1
        total=len(data)
        while idx<total:
            item=data[idx]
            length=match(item)
            if length<0 or idx+length>=total:
                return False
            idx+=1
            for i in range(length):
                if (data[idx]>>6)!=2:
                    return False
                idx+=1
        return True