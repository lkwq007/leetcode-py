class ThroneInheritance:

    def __init__(self, kingName: str):
        self.record={}
        self.record[kingName]=[]
        self.dead={}
        self.order=[]

    def birth(self, parentName: str, childName: str) -> None:
        

    def death(self, name: str) -> None:
        self.dead[name]=1

    def getInheritanceOrder(self) -> List[str]:
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()