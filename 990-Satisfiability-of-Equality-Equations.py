class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # only lower case letters
        disjoint=[-1]*128
        def find(x):
            idx=x
            while disjoint[idx]!=-1:
                idx=disjoint[idx]
            while disjoint[x]!=-1:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        for item in equations:
            if item[1]=="=":
                a_idx=find(ord(item[0]))
                b_idx=find(ord(item[3]))
                if a_idx!=b_idx:
                    disjoint[b_idx]=a_idx
            else:
                if item[0]==item[3]:
                    return False
        for item in equations:
            if item[1]=="!":
                a_idx=find(ord(item[0]))
                b_idx=find(ord(item[3]))
                if a_idx==b_idx:
                    return False
        return True
