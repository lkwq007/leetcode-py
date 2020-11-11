class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        lst=[p1,p2,p3,p4]
        vector=[(lst[i][0]-p1[0],lst[i][1]-p1[1]) for i in range(1,4)]
        def norm(vec):
            return vec[0]*vec[0]+vec[1]*vec[1]
        for i in range(3):
            for j in range(i+1,3):
                if vector[i][0]*vector[j][0]+vector[i][1]*vector[j][1]==0 and norm(vector[i])==norm(vector[j]) and norm(vector[i])>0:
                    for k in range(3):
                        if k!=i and k!=j:
                            if vector[k][0]==vector[i][0]+vector[j][0] and \
                                vector[k][1]==vector[i][1]+vector[j][1]:
                                return True
        return False