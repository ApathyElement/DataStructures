class Node(object):
    def __init__(self, data, left = None, right = None, previous = None):
        self.data = data
        self.left = left
        self.right = right
        self.previous = previous
    def __str__(self) -> str:
        return '(' + str(self.left) + ', ' + str(self.prevData) + '->' + str(self.data) + ', ' + str(self.right) + ')'
    
    @property
    def prevData(self):
        return self.previous.data if self.previous != None else 'O'
    
    @property
    def prev(self):
        return self.previous if self.previous != None else None

    @property
    def childNo(self):
        childno = 0
        if self.left == None:
            childno += 1

        if self.right == None:
            childno += 1
        return childno

    @property
    def is_leaf(self):
        return (self.left == None and self.right == None)

    def UpdateNodeFromData(self, data):
        if data == self.data:
            return self
        if data > self.data:
            self.right = Node(data, previous=self)
            return self.right
        else:
            self.left = Node(data, previous=self)
            return self.left

    def deleteNodeWithData(self, data):
        if self.left != None:
            if self.left.data == data:
                self.left = None
        if self.right != None:
            if self.right.data == data:
                self.right = None


    

class BinaryTree(object):
    def __init__(self, inarr = None):
        self.root = None
        for x in inarr:
            self.append(x)

    def __str__(self) -> str:
        return str(self.root)
        
        
    def inorderPredecessor(self, node):
        #rightmost node of the left subtree
        if node.left == None:
            

    def inorderSuccessor(self, node):
        #leftmost node of the right subtree
        pass
    

    def search(self,data) -> Node:

        def searchSubtree(node) -> Node:
            if node == None:
                return None

            if node.data == data:
                return node

            return searchSubtree(node.right) if data > node.data else searchSubtree(node.left)

        return searchSubtree(self.root)


    def append(self, data) -> Node:
        def appendToSubtree(node, data) -> Node:
            if node.is_leaf:
                rNode = node.UpdateNodeFromData(data)
                return rNode
            else:
                if data == node.data:
                    return node
                if data > node.data:
                    if node.right == None:
                        return node.UpdateNodeFromData(data)
                    else:
                        return appendToSubtree(node.right, data)
                if data < node.data:
                    if node.left == None:
                        return node.UpdateNodeFromData(data)
                    else:
                        return appendToSubtree(node.left, data)

        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            return appendToSubtree(self.root, data)



    def delete(self,data) -> None:
        rNode = self.search(data)
        if rNode == None:
            return False

        if rNode.is_leaf:
            rNode.prev.deleteNodeWithData(data)
            return True

        if rNode.childNo == 1:
            if rNode.left == None:
                cNode = rNode.right
            else:
                cNode = rNode.left
            
            pNode = rNode.prev

            cNode.previous = pNode
            if cNode.data > pNode.data:
                pNode.right = cNode
            else:
                pNode.left = cNode

        if rNode.childNo == 2:
            pass

            
        
            





            
        


