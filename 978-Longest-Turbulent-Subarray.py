class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ret=1
        last=arr[0]
        acc=1
        flag=None
        for item in arr[1:]:
            if item==last:
                acc=1
                flag=None
            elif item>last:
                if flag is None:
                    acc+=1
                    flag=True
                elif flag:
                    acc=2
                else:
                    acc+=1
                flag=True
            else:
                if flag is None:
                    acc+=1
                elif flag:
                    acc+=1
                else:
                    acc=2
                flag=False
            last=item
            ret=max(ret,acc)
        return ret