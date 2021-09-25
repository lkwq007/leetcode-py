class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.ret=[]
        def check(lst):
            for i in range(len(lst)-1):
                if i>0 and lst[i-1] in "+-*" and lst[i]=="0" and lst[i+1] not in "+-*" or i==0 and lst[i]=="0" and lst[i+1] not in "+-*":
                    return True
            return False
        def probe(idx,acc):
            if idx>=len(num):
                if check(acc):
                    return
                if eval(acc)==target:
                    self.ret.append(acc)
                return
            probe(idx+1,acc+num[idx])
            for op in "+-*":
                probe(idx+1,acc+op+num[idx])
        probe(1,num[0])
        return self.ret