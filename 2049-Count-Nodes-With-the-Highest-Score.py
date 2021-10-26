class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        if len(parents)<2:
            return len(parents)-1
        left=[-1]*len(parents)
        right=[-1]*len(parents)
        cnt=[0]*len(parents)
        total=len(parents)
        ret=0
        max_val=total-1
        for i in range(1,len(parents)):
            item=parents[i]
            if left[item]==-1:
                left[item]=i
            else:
                right[item]=i
        lst=[]
        for i in range(len(parents)):
            if left[i]==-1 and right[i]==-1:
                lst.append(i)
        queue=lst
        visited=[0]*len(parents)
        while queue:
            target=[]
            for item in queue:
                if visited[item]==1:
                    continue
                visited[item]=1
                score=1
                rest=total-1
                cnt[item]=1
                if left[item]!=-1:
                    score*=cnt[left[item]]
                    rest-=cnt[left[item]]
                    cnt[item]+=cnt[left[item]]
                if right[item]!=-1:
                    score*=cnt[right[item]]
                    rest-=cnt[right[item]]
                    cnt[item]+=cnt[right[item]]
                if rest>0:
                    score*=rest
                # print(item,score,max_val)
                if score>max_val:
                    ret=1
                    max_val=score
                elif score==max_val:
                    ret+=1
                if item!=0 and visited[parents[item]]==0:
                    par=parents[item]
                    if (left[par]!=-1 and visited[left[par]]!=1) or (right[par]!=-1 and visited[right[par]]!=1):
                        pass
                    else:
                        target.append(par)
            queue=target
        return ret




