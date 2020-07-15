from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ret=[]
        def probe(s,acc):
            if not s:
                self.ret.append(acc)
                return
            item=s[0]
            if item.isalpha():
                probe(s[1:],acc+item.lower())
                probe(s[1:],acc+item.upper())
            else:
                probe(s[1:],acc+item)
        probe(S,"")
        return self.ret


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret=[]
        pos=[]
        template=list(S.lower())
        template_upper=list(S.upper())
        cnt=0
        for idx in range(len(S)):
            if S[idx].isalpha():
                cnt+=1
                pos.append(idx)
        total=1<<cnt
        def set_bits(mask,lst):
            idx=0
            while mask>0:
                if mask&1:
                    lst[pos[idx]]=template_upper[pos[idx]]
                idx+=1
                mask=mask>>1
        for i in range(total):
            tmp=template[:]
            set_bits(i,tmp)
            ret.append("".join(tmp))
        return ret

