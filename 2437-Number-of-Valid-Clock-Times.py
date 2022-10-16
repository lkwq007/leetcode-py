class Solution:
    def countTime(self, time: str) -> int:
        h,m=time.split(":")
        def count(total,val):
            cnt=0
            for i in range(total):
                cur=f"{i:02}"
                if val in [cur,cur[0]+"?","?"+cur[1],"??"]:
                    cnt+=1
            return cnt
        return count(24,h)*count(60,m)