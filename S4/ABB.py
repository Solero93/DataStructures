from class_BTreeNode import*


class BinaryTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, data, key):
        if self.isEmpty():
            self.root = TreeNode(data, key)
        else:
            tmp = self.root
            self.insertRecursive(tmp, None, data, key)

    def insertRecursive(self, root, father, data, key):
        if root is None:
            return TreeNode(data, key, father)
        else:
            if data < root.getKey():
                root.left = self.insertRecursive(root.getLeft(), root, data, key)
            elif data == root.getKey():
                root.getData().append(data)
            else:
                root.right = self.insertRecursive(root.getRight(), root, data, key)
        return root

    def isInRange(self, minim, maxim, root):
        if minim <= root.getKey() <= maxim:
            return True
        return False

    def search(self, minim, maxim):
        tmp = self.root
        return self.searchRec(tmp, minim, maxim)

    def searchRec(self, root, minim, maxim):
        if root is None:
            return []
        elif self.isInRange(minim, maxim, root):
            return self.searchRec(root.getLeft(), minim, maxim) + [root] + self.searchRec(root.getRight(), minim, maxim)
        else:
            return self.searchRec(root.getLeft(), minim, maxim) + self.searchRec(root.getRight(), minim, maxim)

    def remove(self, minim, maxim):
        tmp = self.root
        list = self.searchRec(tmp, minim, maxim)
        for element in list:
            self.generalErase(element)

    # def findToDelete(self, root, minim, maxim):
    #     self.searchRecursive()
        # if root is not None:
        #     self.findToDelete(root.getLeft(), minim, maxim)
        #     self.findToDelete(root.getRight(), minim, maxim)
        #     if self.isInRange(minim, maxim, root):
        #         self.generalErase(root)
        #return root

        # if root is None:
        #     return None
        # else:
        #     if self.isInRange(minim, maxim, root):
        #         print root, root.getFather(), root.grade(), "..",
        #         self.generalErase(root)
        #     return self.findToDelete(root.getLeft(), minim, maxim), self.findToDelete(root.getRight(), minim, maxim)

    def generalErase(self, root):
        print root, root.getFather(), root.grade(), root == self.root, "..",
        if root is self.root:
            self.eraseRoot()
        elif root.grade() == 0:
            self.erase0(root)
        elif root.grade() == 1:
            self.erase1(root)
        else:
            self.erase2(root)

    def eraseRoot(self):
        if self.root.grade() == 0:
            self.root = None
        elif self.root.grade() == 1:
            if self.root.getLeft() is None:
                self.root = self.root.getRight()
            else:
                self.root = self.root.getLeft()
        else:
            maxVal = self.root.getLeft().find_max()
            self.root.setData(maxVal.getData())
            self.root.setKey(maxVal.getKey())
            self.erase0(maxVal)

    def erase0(self, root):
        if root.getFather().left is root:
            root.getFather().setLeft(None)
        else:
            root.getFather().setRight(None)

    def erase1(self, root):
        if root.getFather().getLeft() is root:
            if root.getLeft() is not None:
                root.getFather().setLeft(root.getLeft())
                root.getLeft().setFather(root.getFather())
            else:
                root.getFather().setLeft(root.getRight())
                root.getRight().setFather(root.getFather())
        else:
            if root.getLeft() is not None:
                root.getFather().setRight(root.getLeft())
                root.getLeft().setFather(root.getFather())
            else:
                root.getFather().setRight(root.getRight())
                root.getRight().setFather(root.getFather())

    def erase2(self, root):
        maxVal = root.getLeft().find_max()
        root.setData(maxVal.getData())
        root.setKey(maxVal.getKey())
        self.erase0(maxVal)

    def printTree(self):
        if self.isEmpty():
            print None
        else:
            root = self.root
            self.printRecursive(root)

    def printRecursive(self, root):
        if root.getLeft():
            self.printRecursive(root.getLeft())
        print root,
        if root.getRight():
            self.printRecursive(root.getRight())


def main():
    a = BinaryTree()
    a.insert(8, 8)
    a.insert(0, 0)
    a.insert(16, 16)
    a.insert(-2, -2)
    a.insert(2, 2)
    a.insert(14, 14)
    a.insert(18, 18)
    a.insert(-3, -3)
    a.insert(-1, -1)
    a.insert(1, 1)
    a.insert(3, 3)
    a.insert(13, 13)
    a.insert(15, 15)
    a.insert(17, 17)
    a.insert(19, 19)
    print ""
    a.printTree()
    print ""
    a.remove(-1, 100)
    print ""
    a.printTree()


main()