class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left=int(left)
        right=int(right)
        l=int(sqrt(left))
        r=int(sqrt(right))
        self.ret=0
        lst=["0","1","2","3"]
        for i in range(4):
            if left<=i*i<=right:
                self.ret+=1
        def check(word):
            for i in range(len(word)//2):
                if word[i]!=word[len(word)-i-1]:
                    return False
            return True
        def probe(base):
            if len(base)>9:
                return
            for item in lst:
                tmp=item+base+item
                if tmp[0]!="0":
                    val=int(tmp)
                    val=val*val
                    if left<=val<=right and check(str(val)):
                        # print(tmp)
                        self.ret+=1
                probe(tmp)
        probe("")
        for item in lst:
            probe(item)
        return self.ret
