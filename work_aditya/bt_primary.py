from collections import deque

## TODO
## inorder successor
## postorder successor
## other algos

class Node:
    def __init__(self, val, left=None, right=None):
        self.data=val
        self.right=right
        self.left=left

class BinaryTree:
    def __init__(self, node):
        self.root=node

    
    
    def display(self, node):
        if node== None:
            return 
        res=""
        res+= '.' if node.left==None else str(node.left.data)
        res+= '<-'+str(node.data)+'->'
        res+= '.' if node.right==None else str(node.right.data)
        print(res)
        self.display(node.left)
        self.display(node.right)


    
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

    def height(self, root):
        if root== None:
            return -1

        lefth= self.height(root.left)
        right= self.height(root.right)
        total_height= max(lefth, right)+1
        return total_height
    
    def isBalanced(self, root):
        if root== None: 
            return True

        lh= self.height(root.left)
        rh= self.height(root.right)
        if (abs(lh-rh)<= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True: 
            return True
        
        return False

    def maxDepth(self, root):
        if root== None:
            return -1
        else:
            left_dept= self.maxDepth(root.left)
            right_dept= self.maxDepth(root.right)
            if left_dept> right_dept:
                return left_dept+1
            else:
                return right_dept+1

    def minDepth(self, root):
        mind=0
        if root==None:
            return mind
        
        queue=deque([])
        queue.append(root)
        while len(queue)>0:
            mind+=1
            level_size=len(queue)
            for i in range(level_size):
                current = queue.popleft()
                
                if current.left == None and current.right ==None:
                    return mind
                
                if current.left != None:
                    queue.append(current.left)
                if current.right !=None:
                    queue.append(current.right)
        return mind
    
    def hasPathSum(self, root, targetSum):
        if root==None:
            return False
        
        if root.data==targetSum and root.left==None and root.right==None:
            return True
        return self.hasPathSum(root.left, targetSum-root.data) or self.hasPathSum(root.right, targetSum-root.left)


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
    
    def inorderSuccessor(self, root, p):
        def solve(root, p, successor):
            if root==None : return successor
            if root.data > p.data and (successor == None or root.data < successor.data):
                successor= root
            if p.data >= root.data:
                return solve(root.right, p,successor)
            elif root.left == None:
                return root
            else:
                return solve(root.left, p, successor)

        successor= None
        return solve(root, p, successor)

    
    def lca(self, root, n1, n2):
        while root!=None:
            if root.data > n1 and root.data > n2:
                root = root.left

            elif root.data< n1 and root.data<n2:
                root = root.right
            
            else:
                break
        return root


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

    


# tree.root= Node(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.right.right=Node(5)
# tree.root.left.right=Node(6)
arr=[1,2,3,4,5,6,7,8,9,10]
node= sortedLsToTree(arr)
tree= BinaryTree(node)

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
# print('Level order successor of ',key,': ', tree.levelOrderSuccessor(tree.root, key).data)
print('Minimum Depth: ', tree.minimumDepth(tree.root))
print("Right Veiw: ",tree.rightView(tree.root))
tree.display(tree.root)
