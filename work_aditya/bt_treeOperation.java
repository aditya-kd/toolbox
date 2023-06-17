// import java.util.Scanner;
// //this file holds all the operations on trees


// public class TreeOperations{
     
//     public static void main(String[] args) {
//         //int arr[]={12,25,37,50,62,75,87};
//         print("Do you want to input in  Level Order OR in sorted array form?(1/2)");
//         Scanner sc=new Scanner (System.in);
//         int l=sc.nextInt();        sc.close();
//         int arr[]=accept();
//         Tree root=null;
//         if(l==1)
//         root=createTreeLevel(arr);
//         else
//         root=createTree(arr, 0, arr.length-1);
//         System.out.println("The inputted tree in format is: \n");
//         display(root);
//         print("Size : "+size(root));
//         print("MAX : "+max(root));
//         print("MIN : "+min(root));
//         print("HEIGHT : "+height(root));
//         print("SUM of NODES: "+sum(root));
//         insert(root, 387);
//         print("INSERTING 387:" );
//         display(root);
//         printsl("NEW HEIGHT IS");
//         print(height(root));
//         Tree newnode2=search(root, 62);        
//         String sr1=newnode2==null?"NOT FOUND":"FOUND AT height"+height(newnode2);
//         print("SEARCH 62: "+sr1);
//         Tree newnode3=search(root, 456);        
//         String sr2=newnode3==null?"NOT FOUND":"FOUND AT height"+height(newnode3);
//         print("SEARCH 456: "+sr2);
//         remove(root,87);
//         print("REMOVE 87: ");
//         display(root);
//         if(remove(root, 1987)==null)
//         print("REMOVE 1897: DOES NOT EXIST, NOT REMOVED");
//         print("INORDER");
//         inorder(root);
//         print("POSTORDER");
//         postorder(root);
//         print("PREORDER");
//         preorder(root);        
//         print("LEVEL ORDER");
//         levelOrder(root);
//     }
//     //helper methods to print and return with next line
//     public static <E>void print(E to_be_printed)
//     {
//         System.out.println(to_be_printed+"\n");
//     }
//     //helper method to print and return to same line
//     public static <E>void printsl(E to_be_printed)
//     {
//         System.out.print(to_be_printed+" ");
//     }    
//     public static int[] accept()
//     {   int i=0,n=0;
//         print("Enter the number of elements in the tree");
//         var sc = new Scanner(System.in);
//         n = sc.nextInt();sc.close();
//         int[] treedata=new int[n];       
//         print("Start inputting into tree");
//         sc.reset();
//         for(i=0;i<n;i++)
//         {
//             print("Enter node "+i);
//             treedata[i]=sc.nextInt();
//         }
//         sc.close();
//         return treedata;

//     }

//     public static Tree createTreeLevel(int a[])
//     {
//         if(a.length==0)
//         {
//             return null;
//         }
//         Tree root=null;

//         for(int i=0;i<a.length;i++)
//         {
//             root=cLevelOrder(root, a[i]);
//         }
//         return root;
//     }
//     public static Tree cLevelOrder(Tree root, int data)
//     {
//         if(root==null)
//         {
//             root=new Tree(data);
//             return root;
//         }
//         if(data <= root.data)
//         root.left= cLevelOrder(root.left, data);
//         else
//         root.right=cLevelOrder(root.right, data);
//         return root;
//     }
//     public static Tree createTree(int[] arr, int lo, int hi)
//     {
//         if(lo>hi)return null;
//         int mid=(lo+hi)/2;
//         int data=arr[mid];
//         Tree lc=createTree(arr, lo, mid-1);
//         Tree rc=createTree(arr, mid+1, hi);

//         Tree node= new Tree(data,lc,rc);
//         return node;
//     }
    
//     public static void display(Tree node)
//     {
//         if(node==null)
//         return;
//         String str="";
//         str+=node.left==null?".":node.left.data;
//         str+="<-"+node.data+"->";
//         str+=node.right==null?".":node.right.data;
//         System.out.println(str);
//         display(node.left);
//         display(node.right);
//     }
//     //find the SIZE
//      public static int size(Tree node)
//     {
//         if(node==null)
//         return 0;
//         int ls=size(node.left);
//         int rs=size(node.right);
//         int th=ls+rs+1;
//         return th;
//     }
//     //returning the MAX
//     public static int max(Tree node)
//     {
//         if(node.right!=null)
//         return max(node.right);
//         else return node.data;
//     }
//     //returning the MIN
//     public static int min(Tree node)
//     {
//         if(node.left!=null)
//         return min(node.left);
//         else return node.data;
//     }
//     //sum of nodes upto given node
//     public static int sum(Tree node)
//     {
//         if(node==null)
//         {return 0;}
//         int leftsum=sum(node.left);
//         int rightsum=sum(node.right);
//         int totalsum = leftsum+rightsum+node.data;
//         return totalsum;
//     }
//     //find the height of the tree
//     public static int height(Tree node)
//     {
//         if(node==null)
//         return -1;
//         int leftheight=height(node.left);
//         int rightheight=height(node.right);
//         int totalheight=Math.max(leftheight,rightheight)+1;
//         return totalheight;
//     }
//     //insert a node in tree
//     public static Tree insert(Tree node, int data)
//     {
//         if(node==null)
//         {
//             Tree newnode= new Tree(data,null,null);
//             return newnode;
//         }
//         if(data>node.data);
//         node.right=insert(node.right,data);
//         if(data<node.data)
//         node.left=insert(node.left,data);

//         return node;
//     }
//     //search a data in tree--RECURSIVE, complexity O(n)
//     public static Tree search(Tree node, int key)
//     {   if(node==null||node.data==key)
//         return node;
//         if(key>node.data)
//         return search(node.right,key);
//         if(key<node.data)
//         return search(node.left,key);

//         return node;
//     }
//     //search a key in tree--NON-RECURSIVE, complexity O(logn)
//     public static Tree search2(Tree node, int key)
//     {
//         while(node!=null&&key!=node.data)
//         {
//             if(key<node.data)
//                 node=node.left;
//             else
//                 node=node.right;                
//         }
//         return node;
//     }
//     //remove or delete a key from the tree
//     public static Tree remove(Tree node, int data)
//     {
//         if(node==null)
//         return null;
//         if(data>node.data)
//         node.right=remove(node.right,data);
//         else if(data<node.data)
//         node.left=remove(node.left,data);
//         else{
//             //both child 
//             if(node.left!=null && node.right!=null)
//             {
//                 int leftmax=max(node.left);
//                 node.data=leftmax;
//                 node.left=remove(node.left,leftmax);
//                 return node;
//             }
//             else if(node.left!=null)
//             return node.left;
//             else if(node.right!=null)
//             return node.right;
//             else return null;
//         }
//             return node;
        
//     }
//     //level order tree traversal
//     public static void levelOrder(Tree root)
//     {
        
//         for(int i=0;i<=height(root);i++)
//         getAtLevel(root,i);                
//     }
//     //helper method for levelORder
//     public static void getAtLevel(Tree root, int level)
//     {
//         if(root==null)return ;
//         if(level==0)
//         printsl(root.data);
//         else if(level>0)
//         {
//             getAtLevel(root.left, level-1);
//             getAtLevel(root.right, level-1);
//         }
      
//     }
//     //postorder tree traversal
//     public static Tree postorder(Tree root)
//     {
//         if(root==null)return null;
//         postorder(root.left);
//         postorder(root.right);
//         print(root.data);
//         return root;
//     }
//     //preorder traversal of the tree
//     public static Tree preorder(Tree root)
//     {
//         if(root==null)return null;
//         print(root.data);
//         preorder(root.left);
//         preorder(root.right);
//         return root;
//     }
//     //inorder traveral of tree
//     public static Tree inorder(Tree root)
//    j  {
//         if(root==null)return null;
//         inorder(root.left);
//         print(root.data);
//         inorder(root.right);
//         return root;
//     }
    
// }