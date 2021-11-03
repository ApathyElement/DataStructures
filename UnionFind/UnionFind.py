from dataclasses import dataclass
from typing import Union
@dataclass
class Node:
    name: str
    root: int
class UnionFind(object):
    def __init__(self, Items: list[str]) -> None :
        self.data = []
        self.pos = {}
        for item in Items:
            self.pos[item] = len(self.data)
            self.data.append(Node( item, len(self.data)))


    def __str__(self) -> str:
        output = '{'
        for node in self.data:
            output += f'( {node.name} : {self.pos[node.name]} -> {node.root} )'
            output += ' , '
        output += '}'
        
        return output

    def getPosition(self, node:Node)-> str:
        return self.pos[node.name]

    def getNode(self, name: Union[str,int], root=None) -> Node:
        if root != None:
            return self.data[root]

        if type(name) is str:
            if name not in self.pos.keys():
                return None

            leaf = self.pos[name]
            return self.data[leaf]

        if type(name) is int:
            return self.data[name]

    def find(self, name:Union[Node,str]) -> int:
        
        if type(name) is str:
            node =  self.getNode(name)

        if type(name) is Node:
            node = name

        if node == None:
            return None

        if self.getPosition(node) == node.root:
            return node.root
        else:
            return self.find(self.getNode(node.name, node.root))

    @property
    def components(self):
        outDict = {}
        for node in self.data:
            rootNode = self.data[self.find(node)]
            if rootNode.root in outDict.keys():
                outDict[rootNode.root].append(node.name)
            else:
                outDict[rootNode.root] = [node.name]

        return outDict


    def unify(self, item1:str, item2:str) -> bool:
        item1root = self.getNode(item1)
        item2root = self.getNode(item2)

        if item1root == None or item2root == None:
            return False

        item1root.root = item2root.root
        return True

        
        


    