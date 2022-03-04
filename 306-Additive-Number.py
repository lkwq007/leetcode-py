class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def probe(pos,last,total):
            for i in range(pos,len(num)):
                cur=int(num[pos:i+1])
                if cur==total and (i+1==len(num) or probe(i+1,total,last+total)):
                    return True
                if num[pos]=="0":
                    break
            return False
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                first=int(num[:i+1])
                second=int(num[i+1:j+1])
                if probe(j+1,second,first+second):
                    return True
                if num[i+1]=="0":
                    break
            if num[0]=="0":
                break
        return False
                
