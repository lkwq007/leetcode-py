class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        record={}
        min_len=len(strs[0])
        for i in range(len(strs)):
            item=strs[i]
            total=len(item)
            min_len=max(total,min_len)
            if total not in record:
                record[total]=[]
            record[total].append(i)
        def is_sub(a,b):
            i=0
            for j in range(len(b)):
                if a[i]==b[j]:
                    i+=1
                if i==len(a):
                    return True
            return False
        lst=reversed(sorted(record.keys()))
        for key in lst:
            for idx in record[key]:
                flag=True
                for i in range(len(strs)):
                    if i!=idx and is_sub(strs[idx],strs[i]):
                        flag=False
                if flag:
                    return key
        return -1
        