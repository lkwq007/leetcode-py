class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=0
        d=0
        for item in senate:
            if item=="R":
                r+=1
        d=len(senate)-r
        record={}
        record["R"]=r
        record["D"]=d
        stack=[]
        lst=senate
        while record["R"]>0 and record["D"]>0:
            target=[]
            for item in lst:
                if stack and stack[-1]!=item:
                    top=stack.pop()
                    record[item]-=1
                    target.append(top)
                else:
                    stack.append(item)
            lst=target
        return "Radiant" if record["R"]>0 else "Dire"