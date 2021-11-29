class ThroneInheritance:

    def __init__(self, kingName: str):
        self.tree = defaultdict(list)
        self.tree[kingName] = []
        self.dea = {}
        self.king = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dea[name] = True

    def getInheritanceOrder(self) -> List[str]:
        arr = []
        def dfs(i):
            if i not in self.dea:
                arr.append(i)
            for j in self.tree[i]:
                dfs(j)
        dfs(self.king)
        return arr