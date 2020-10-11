class Solution:
    def smallestSubsequence(self, text: str) -> str:
        # only lowercase
        s=text
        record={}
        for item in s:
            record[item]=record.get(item,0)+1
        stack=[]
        ret={}
        for item in s:
            if ret.get(item,0)>0:
                record[item]-=1
                continue
            while stack and stack[-1]>=item and record[stack[-1]]>1:
                top=stack.pop()
                record[top]-=1
                ret[top]-=1
            if ret.get(item,0)==0:
                ret[item]=1
                stack.append(item)
        return "".join(stack)