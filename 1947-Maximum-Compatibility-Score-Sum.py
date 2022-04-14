class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        compat=[[0]*len(mentors) for _ in students]
        for i in range(len(students)):
            for j in range(len(mentors)):
                acc=0
                for k in range(len(students[i])):
                    if students[i][k]==mentors[j][k]:
                        acc+=1
                compat[i][j]=acc
        import functools
        mapping=[0]*len(students)
        mask=1
        for i in range(len(mapping)):
            mapping[i]=mask
            mask=mask<<1
        @functools.lru_cache(None)
        def probe(acc,pos):
            if pos>=len(mentors):
                return 0
            ret=0
            for i in range(len(mapping)):
                if mapping[i]&acc==0:
                    ret=max(ret,compat[i][pos]+probe(acc|mapping[i],pos+1))
            return ret
        return probe(0,0)
