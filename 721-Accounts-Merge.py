class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mapping={}
        disjoint=[-1]*len(accounts)
        def find(x):
            idx=x
            while disjoint[idx]!=-1:
                idx=disjoint[idx]
            while disjoint[x]!=-1:
                tmp=disjoint[x]
                disjoint[x]=idx
                x=tmp
            return idx
        def union(a,b):
            a_idx=find(a)
            b_idx=find(b)
            if a_idx!=b_idx:
                disjoint[b_idx]=a_idx
            return a_idx
        for i,account in enumerate(accounts,0):
            name=accounts[0]
            for email in account[1:]:
                if email in mapping:
                    union(mapping[email],i)
                else:
                    mapping[email]=i
        record={}
        for email,idx in mapping.items():
            set_idx=find(idx)
            if set_idx not in record:
                record[set_idx]=[]
            record[set_idx].append(email)
        for key,val in record.items():
            val.sort()
            val.insert(0,accounts[key][0])
        return [item for item in record.values()]