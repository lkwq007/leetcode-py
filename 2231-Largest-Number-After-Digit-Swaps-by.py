class Solution:
    def largestInteger(self, num: int) -> int:
        lst=list(str(num))
        odd=[i for i in range(len(lst)) if int(lst[i])%2]
        even=[i for i in range(len(lst)) if int(lst[i])%2==0]
        odd.sort(key=lambda x:-int(lst[x]))
        even.sort(key=lambda x:-int(lst[x]))
        ret=[]
        i0=0
        i1=0
        for i in range(len(lst)):
            if int(lst[i])%2:
                ret.append(lst[odd[i0]])
                i0+=1
            else:
                ret.append(lst[even[i1]])
                i1+=1
        return int("".join(ret))

