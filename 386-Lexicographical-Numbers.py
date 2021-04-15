class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        cnt=1
        ret=[1]
        while cnt<n:
            cnt+=1
            val=ret[-1]
            if val*10<=n:
                val*=10
            elif val+1<=n and (val+1)//10==(val)//10:
                val+=1
            else:
                val=val//10
                while (val+1)//10!=(val)//10:
                    val=val//10
                val+=1
            ret.append(val)
        return ret