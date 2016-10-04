import copy

class BinaryTreeNode():
    def __init__(self, data=None):
        self.node = [data,[],[]]
        
    def __cmp__(self,other):
        if self.node[0] < other[0]:
            return -1
        if self.node[0] == other[0]:
            return 0
        else:
            return 1
	
    def __str__(self):
        return str(self.node[0])
    
    def getData(self):
	return self.node[0]    
    def setData(self,data):
	self.node[0] = data
    
    def getLeft(self):
	return self.node[1]    
    def setLeft(self,node):
	self.node[1] = node
    
    def getRight(self):
	return self.node[2]    
    def setRight(self,node):
	self.node[2] = node
        

class BinaryTree():
    def __init__(self, root=None):
        self.root = BinaryTreeNode(root)
        
    def add(self, item):
	itemNode = BinaryTreeNode(item)
	
	if self.isEmpty():
	    self.root = itemNode
	else:
	    tmp = copy.copy(self.root)
	    while tmp.getLeft() != None and tmp.getRight() != None:
		if itemNode < tmp.getLeft() or (itemNode > tmp.getLeft() and itemNode < tmp.getRight()):
		    tmp = tmp.getLeft()
		elif itemNode == tmp.getLeft():
		    tmp.getLeft.setData(tmp.getLeft.getData(), itemNode.getData())
		    return
		elif itemNode == tmp.getRight():
		    tmp.getRight.setData(tmp.getRight.getData(), itemNode.getData())
		    return		    
		elif itemNode > tmp.getLeft():
		    if itemNode < tmp.getRight():
			tmp = tmp.getLeft()
	    
	    
	    if tmp.getLeft() == None and tmp.getRight != None:
		if tmp.getRight() > itemNode:
		    tmp.setLeft(itemNode)
		else:
		    tmp.setLeft(tmp.getRight())
		    tmp.setRight(itemNode)
	    else:
		
		
	    
    def isEmpty(self):
	return self.root == None

    def getRootVal(self):
	return self.root.data
    
    def getLeftChild(self):
	    #si no esta vacío retorna el subárbol izquierdo de la raíz

    def getRightChild(self):
	    #si no esta vacío retorna el subárbol derecho de la raíz

    def insertRight(self, val):

    def insertLeft(self,val):

    def setRootVal(self,val):
	pass
        