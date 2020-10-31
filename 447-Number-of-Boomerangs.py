class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret=0
        for i in range(len(points)):
            record={}
            for j in range(len(points)):
                if j==i:
                    continue
                x_dist=points[i][0]-points[j][0]
                y_dist=points[i][1]-points[j][1]
                dist=x_dist*x_dist+y_dist*y_dist
                record[dist]=record.get(dist,0)+1
            for k,v in record.items():
                ret+=v*(v-1)
        return ret
