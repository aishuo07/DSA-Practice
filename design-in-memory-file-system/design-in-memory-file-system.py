class FileSystem:

    def __init__(self):
        self.dic = {}
        
    def ls(self, path: str) -> List[str]:
        print(self.dic)
        c = path[1:].split('/')
        dic = self.dic
        for i in c:
            if i in dic:
                dic = dic[i]
        
        if type(dic) == dict:
            return sorted(dic.keys())
        return [c[-1]]
    
    def mkdir(self, path: str) -> None:
        c = path[1:].split('/')
        dic = self.dic
        for i in c:
            if i not in dic:
                dic[i] = {}
            dic = dic[i]
        

    def addContentToFile(self, path: str, content: str) -> None:
        c = path[1:].split('/')
        dic = self.dic
        for i in c[:-1]:
            if i not in dic:
                dic[i] = {}
            dic = dic[i]
        if c[-1] in dic:
            dic[c[-1]] += content
        else:
            dic[c[-1]] = content

    def readContentFromFile(self, path: str) -> str:
        c = path[1:].split('/')
        dic = self.dic
        for i in c[:-1]:
            if i not in dic:
                dic[i] = {}
            dic = dic[i]
        return dic[c[-1]]