class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        record={}
        indegree=[len(item) for item in ingredients]
        graph={}
        for idx in range(len(recipes)):
            for item in ingredients[idx]:
                if item not in graph:
                    graph[item]=[]
                graph[item].append(idx)
        queue=supplies
        ret=[]
        while queue:
            target=[]
            for item in queue:
                for next in graph.get(item,[]):
                    indegree[next]-=1
                    if indegree[next]==0:
                        target.append(recipes[next])
            queue=target
        return [recipes[i] for i in range(len(recipes)) if indegree[i]==0]

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        record={}
        for item in supplies:
            record[item]=1
        queue=[i for i in range(len(recipes))]
        ret=[]
        while queue:
            target=[]
            for idx in queue:
                cnt=0
                for item in ingredients[idx]:
                    if item in record:
                        cnt+=1
                if cnt==len(ingredients[idx]):
                    ret.append(recipes[idx])
                    record[recipes[idx]]=1
                else:
                    target.append(idx)
            if len(queue)==len(target):
                break
            queue=target
        return ret