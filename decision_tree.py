class Node:
    i = int()
    __id__ = int()
    __type__ = bool()

    def __init__(self, i, t, id = None):
        self.i = i
        self.setType(t)
        self.id = id
        self.children = dict()
    def setType(self, t):
        self.__type__ = t

    def getType(self):
        return self.__type__

class DecisionTree:
    
    graph = dict()
    head = None

    def setHead(self, head):
        self.head = head

    def setMap(self, case):
        self.map = {i:case[i] for i in range(0, len(case))}

    def compile(self, case):
        current = self.head
        self.setMap(case)
        if (current.getType() == False):
            return self.execute(current)
        else:
            return current.i

    def execute(self, current):
        if (current.getType() == False):
            return self.execute(current.children[self.map[current.i]])
        else:
            return current.i
    
    def getNode(self, nodeData):
        current = self.head
        if (current != None): 
            return self.__getNode__(current, nodeData)
    
    def __getNode__(self, current, nodeData):
        if (current.i == nodeData[0] and current.getType() == nodeData[1] and current.id == nodeData[2]):
            return current
        else:
            wanted_node = None
            for i in current.children:
                wanted_node = self.__getNode__(current.children[i], nodeData)
                if (wanted_node != None):
                    return wanted_node

    def addWay(self, node, way):
        self.graph[node] = way
    
    def buildTree(self, graph):
        Nodes = []
        #{(i, type) : ((i, type), branch)}
        for key in graph:
            r = self.getNode(key)
            root = None
            if (r == None):
                root = Node(key[0], key[1], key[2])
            else:
                root = r
            if (self.head == None):
                self.setHead(root)
            a = graph[key]
            for i in graph[key]:
                r = self.getNode(i[0])
                if (r == None):
                    if (i[0][1] == True):
                        temp_node = Node(i[0][0], True)
                    else:
                        temp_node = Node(i[0][0], i[0][1], i[0][2])
                    root.children[i[1]] = temp_node
                else:
                    root.children[i[1]] = r
