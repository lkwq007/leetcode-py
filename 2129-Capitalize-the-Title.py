class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ret=[]
        for item in title.split(" "):
            if len(item)<3:
                ret.append(item.lower())
            else:
                ret.append(item[0].upper()+item[1:].lower())
        return " ".join(ret)