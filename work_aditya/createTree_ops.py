
class Node:
    def __init__(self, val, left=None, right=None):
        self.data=val
        self.right=right
        self.left=left

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
def display( node):
        if node== None:
            return 
        res=""
        res+= '.' if node.left==None else str(node.left.data)
        res+= '<-'+str(node.data)+'->'
        res+= '.' if node.right==None else str(node.right.data)
        print(res)
        display(node.left)
        display(node.right)

def inorderSuccessor(root, p):
    
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


print("enter number of nodes")
n= int(input())
arr=[]
# arr=list(map(int, input().split()))
arr=[1,2,3,4,5,6]
root= sortedLsToTree(arr)
display(root)
print(root.right.data)
ans = inorderSuccessor(root, root.right)
print('Successor', ans.data)





