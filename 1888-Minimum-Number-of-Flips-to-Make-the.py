class Solution:
    def minFlips(self, s: str) -> int:
        acc0=0
        val0=0
        acc1=0
        lst0=[0]*(len(s)+1)
        lst1=lst0[:]
        for i in range(len(s)):
            if int(s[i])==val0:
                acc1+=1
            else:
                acc0+=1
            lst0[i]=acc0
            lst1[i]=acc1
            val0=1-val0
        # different with odd length
        ret=min(acc0,acc1)
        if len(s)%2:
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    if s[i]=="0":
                        if i%2==0:
                            cur=lst0[i]+lst1[len(s)-1]-lst1[i]
                        else:
                            cur=lst1[i]+lst0[len(s)-1]-lst0[i]
                    else:
                        if i%2==0:
                            cur=lst1[i]+lst0[len(s)-1]-lst0[i]
                        else:
                            cur=lst0[i]+lst1[len(s)-1]-lst1[i]
                    # print(cur)
                    ret=min(ret,cur)
        return ret

class Solution:
    def minFlips(self, s: str) -> int:
        val0=0
        lst=[[0]*(len(s)+1),[0]*(len(s)+1)]
        for i in range(len(s)):
            lst[1][i]=int(int(s[i])==val0)+lst[1][i-1]
            lst[0][i]=int(int(s[i])!=val0)+lst[0][i-1]
            val0=1-val0
        ret=min(lst[0][-2],lst[1][-2])
        if len(s)%2:
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    val=(i%2)^(int(s[i]))
                    cur=lst[val][i]+lst[1-val][len(s)-1]-lst[1-val][i]
                    ret=min(ret,cur)
        return ret