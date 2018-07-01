#coding=utf-8
#! usr/bin/python

'''
二叉树的演示
'''

# (5) 类定义
class Node (object):

    # 结点初始化
    # 添加状态变量 ， A--Active ， R -- Removed
    def __init__(self,data=0,leftChild=None,rightChild=None,status="A"):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.status = status
    # 是否叶子结点
    def isLeaf(self):
        if self.leftChild is None and self.rightChild is None :
            return True
        else:
            return False

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def removeNode(self):
        self.status = "R"

    def activateNode(self):
        self.status = "A"

    def isActiveNode(self):
        return self.status == "A"

class BTree (object):

    def __init__(self,root):
        if  isinstance(root,Node) :
            self.root = root
        else:
            raise TypeError , "root is not an Node."

    def findMin(self,node):
        if (node.hasLeftChild()):
            node = self.findMin(node.leftChild)
        return node

    def search(self,data):
        print " func : search data"
        return self._searchNode(self.root,data)

    def insert(self,data):
        print " func : insert data"
        self._insertNode(self.root,data)

    def remove(self,data):
        print " func : remove data"
        #常规删除，将结点从树中除去
        # self._removeNode(self.root,data)
        #懒惰删除，将其状态位设为非活动
        self._searchNode(self.root,data).removeNode()

    def showDatas(self):
        self._showelements(self.root)

    def _showelements(self,node):
        if (node is not None ):
            self._showelements(node.leftChild)
            if (node.isActiveNode()):
                print "([%s,%s])" % (node.data,node.status)
            self._showelements(node.rightChild)

#   to search a data whether it is in the BTree.
    def _searchNode(self,node,data):
        if node is None:
            print "%s can not be found in this BTree" % (data)
            return None
        elif node.data == data :
            print "%s can be found in this BTree" % (data)
            return node
        elif node.data > data :
            return self._searchNode(node.leftChild,data)
        elif node.data < data :
            return self._searchNode(node.rightChild,data)

#   to insert a data into a BTree
    def _insertNode(self,node,data):
        if node is None:
            return Node(data)
        elif node.data > data :
            node.leftChild = self._insertNode(node.leftChild,data)
        elif node.data < data :
            node.rightChild = self._insertNode(node.rightChild,data)
        else:
            pass

        return node

    def _removeNode(self,node,data):
        if node is None:
            return node

        if node.data > data :
            node.leftChild = self._removeNode(node.leftChild,data)
        elif node.data < data :
            node.rightChild = self._removeNode(node.rightChild,data)
        else:
            if node.isLeaf():
                return None
            elif node.leftChild is not None and node.rightChild is not None:
                node.data = self.findMin(node.rightChild)
                node.rightChild = self._removeNode(node.rightChild,node.data)
            else:
                node = node.leftChild \
                if node.leftChild is not None else \
                node.rightChild

# (7) 主程序
if __name__ == '__main__':
    node = Node(10)
    tree = BTree(node)

    print tree.search(12)
    print tree.search(10)
    tree.insert(9)
    tree.insert(19)
    tree.insert(-9)
    tree.insert(-19)
    tree.insert(29)

    node = tree.findMin(tree.root.rightChild)
    print node.data

    tree.showDatas()

    print "root data is : %d" % (tree.root.data)

    tree.remove(-9)

    print 'chk point 1'
    tree.showDatas()

'''
    below wou't be executed
    # raise excetion if BTree is not initiazed by a node
    tree2 = BTree(12)
    # Not be executed
    print isinstance(12,Node)
'''
