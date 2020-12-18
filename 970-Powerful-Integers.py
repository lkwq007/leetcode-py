class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound<2:
            return []
        x_lst=[1]
        y_lst=[1]
        acc=x
        while acc<=bound and x!=1:
            x_lst.append(acc)
            acc*=x
        acc=y
        while acc<=bound and y!=1:
            y_lst.append(acc)
            acc*=y
        ret=set([])
        for a in x_lst:
            for b in y_lst:
                if a+b<=bound:
                    ret.add(a+b)
                else:
                    break
        return list(ret)