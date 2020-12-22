class Solution:
    def reformatNumber(self, number: str) -> str:
        lst=[""]
        for item in number:
            if item.isnumeric():
                if len(lst[-1])==3:
                    lst.append(item)
                else:
                    lst[-1]+=item
        if len(lst[-1])==1:
            lst[-1]=lst[-2][-1]+lst[-1]
            lst[-2]=lst[-2][:2]
        return "-".join(lst)