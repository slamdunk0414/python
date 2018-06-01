
class Node():

    def __init__(self,item):
        self.elem = item
        self.lChild = None
        self.rChild = None

class Tree():

    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)

        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:

            cur_node = queue.pop(0)

            if cur_node.lChild is None:
                cur_node.lChild = node
                return
            else:
                queue.append(cur_node.lChild)

            if cur_node.rChild is None:
                cur_node.rChild = node
                return
            else:
                queue.append(cur_node.rChild)

    '''先序遍历 先根 再左再右'''
    '''中序遍历 左 根 右'''
    '''后序遍历 左 右 根'''

    def breadth_travel(self):
        '''广度遍历
            先将root放入队列 然后从队列里面取出 如果有左右孩子 则将孩子放入队列 再循环判断
        '''
        if self.root is None:
            print('什么都没有 别遍历了')
            return
        queue = [self.root]

        while queue:

            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lChild is not None:
                queue.append(cur_node.lChild)
            if cur_node.rChild is not None:
                queue.append(cur_node.rChild)

    def preorder(self, node):
        print(node.elem)

        if node.lChild is not None:
            self.preorder(node.lChild)
        if node.rChild is not None:
            self.preorder(node.rChild)

    def midorder(self, node):

        if node.lChild is not None:
            self.midorder(node.lChild)
        print(node.elem +' ' , end='')
        if node.rChild is not None:
            self.midorder(node.rChild)

    def postorder(self, node):

        if node.lChild is not None:
            self.postorder(node.lChild)
        if node.rChild is not None:
            self.postorder(node.rChild)
        print(node.elem + ' ', end='')

t = Tree()

t.add('a')
t.add('b')
t.add('c')
t.add('d')
t.add('e')
t.add('f')
t.add('g')
t.add('h')
t.add('i')
t.add('j')



t.postorder(t.root)



