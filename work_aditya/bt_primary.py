from collections import deque

class Node:
    def __init__(self, val):
        self.data=val
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def sortedLsToTree(arr):
        def createTree(arr, lo, hi):
            if lo>hi: return None
            mid= (lo+hi)//2
            data= arr[mid]
            treeNodeleft= createTree(arr, lo, mid-1)
            treeNoderight= createTree(arr, mid+1, hi)
            
            node= Node(data, treeNodeleft, treeNoderight )
            return node
        #gives the node of the tree
        return createTree(arr, 0, len(arr)-1)
    
    def preorder(self, root):
        if root ==None:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)

    def postorder(self, root):
        if root==None: return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=' ')

    def numberOfNodes(self, root):
        if root==None:
            return 0
        return 1+ self.numberOfNodes(root.left)+self.numberOfNodes(root.right)

    def numLeafNodes(self, root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.numLeafNodes(root.left)+ self.numLeafNodes(root.right)

    def numNonLeafNodes(self, root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 0

        return 1 + self.numNonLeafNodes(root.left)+self.numNonLeafNodes(root.right)

    def numFullNodes(self, root):
        if root==None:
            return 0
        if root.left==None or root.right==None:
            return 0
        ans=0
        if root.left!=None and root.right!=None:
            ans=1
        return ans+self.numNonLeafNodes(root.left)+self.numNonLeafNodes(root.right)

    def levelOrder(self, root):#uses bfs (breadth) not depth
        bfs = []
        if root ==None:
            return bfs
        queue = deque([])
        queue.append(self.root)
        while len(queue) !=0:
            level_size= len(queue)
            current_level= []
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.data)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
            bfs.append(current_level)
        return bfs
        
    def levelOrderBottomUp(self, root):
        bfs=deque([])
        if root==None:
            return bfs
        queue= deque([])
        queue.append(self.root)
        while len(queue)>0:
            level_size=len(queue)
            storecurLevel=[]
            for i in range(level_size):
                currNode= queue.popleft()
                storecurLevel.append(currNode.data)
                if currNode.left!=None:
                    queue.append(currNode.left)
                if currNode.right!=None:
                    queue.append(currNode.right)
            bfs.appendleft(storecurLevel)
        return bfs
                
    
    def zigzag(self, root):
        bfs=[]
        left_to_right=True
        if root == None:
            return bfs
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            current_level = deque()
            for i in range(level_size):
                current = queue.popleft()
                if left_to_right:
                    current_level.append(current.data)
                else:
                    current_level.appendleft(current.data)
                
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
                
            bfs.append(current_level)
            left_to_right = not left_to_right
        return bfs
    
    def levelOrderSuccessor(self, root, key):
        if root == None:
            return None
        queue = deque()
        queue.append(root)
        while len(queue)>0:
            current = queue.popleft()
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
            
            if current.data == key:
                break
        return queue.popleft()

    def minimumDepth(self, root):
        mind=0
        if root == None:
            return mind
        queue = deque([])
        queue.append(self.root)
        while len(queue) !=0:
            mind +=1
            level_size= len(queue)
            for i in range(level_size):
                current = queue.popleft()
                if current.left == None and current.right == None:
                    return mind
                
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
        return mind


    def rightView(self, root):
        result=[]
        if root ==None:
            return result
        queue = deque([])
        queue.append(self.root)
        while len(queue)!=0:
            level_size=len(queue)
            for i in range(level_size):
                current= queue.popleft()
                if i==level_size-1:
                    result.append(current.data)
                if current.left != None:
                    queue.append(current.left)
                if current.right !=None:
                    queue.append(current.right)

        return result

tree= BinaryTree()
tree.root= Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.right.right=Node(5)
tree.root.left.right=Node(6)
print('\nPreorder')
tree.preorder(tree.root)
print('\nInorder')
tree.inorder(tree.root)
print('Postorder')
tree.postorder(tree.root)
print()
print('Number of Nodes:',tree.numberOfNodes(tree.root))
print('Leaf Nodes: ', tree.numLeafNodes(tree.root))
print('Non Leaf Nodes: ', tree.numNonLeafNodes(tree.root))
print('Full Nodes: ', tree.numFullNodes(tree.root))
print('Level Order', tree.levelOrder(tree.root))
key=4
print('Level order successor of ',key,': ', tree.levelOrderSuccessor(tree.root, key).data)
print('Minimum Depth: ', tree.minimumDepth(tree.root))
print("Right Veiw: ",tree.rightView(tree.root))