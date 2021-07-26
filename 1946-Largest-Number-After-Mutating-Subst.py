class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        lst=list(num)
        flag=False
        for i in range(len(lst)):
            item=int(lst[i])
            if change[item]>item:
                lst[i]=str(change[item])
                flag=True
            elif flag and change[item]<item:
                break
        return "".join(lst)