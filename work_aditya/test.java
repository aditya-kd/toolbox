// import java.io.*;
// import java.util.*;
 
// class GFG{
//      public static int sum;
       
// // Recursive function to print all
// // possible subsequences for given array
// public static void printSubsequences(List<Integer> arr, int index,
//                                      ArrayList<Integer> path)
// {
     
//     // Print the subsequence when reach
//     // the leaf of recursion tree
//     if (index == arr.length)
//     {
         
//         // Condition to avoid printing
//         // empty subsequence
//         if (path.size() > 0){}
//         //    System.out.println(path);
//     }
     
//     else
//     {
         
//         // Subsequence without including
//         // the element at current index
//         printSubsequences(arr, index + 1, path);
         
//         path.add(arr[index]);
         
//         // Subsequence including the element
//         // at current index
//         printSubsequences(arr, index + 1, path);
//        //   System.out.println(path);
//          int  max=path.get(0);
//          int  min=path.get(0);

//           for(int i=0; i<path.size(); i++){
            
//             if (path.get(i) > max){
//                 max = path.get(i);}
//           }
//            for(int i=0; i<path.size(); i++){
            
//             if (path.get(i) < min){
//                 min = path.get(i);}
//           }

//           sum+=min*max;
//       //   System.out.println(sum);

//         // Backtrack to remove the recently
//         // inserted element
//         path.remove(path.size() - 1);
//     }
//     return;
// }
 
// // Driver code
// public static void main(String[] args)
// {
//     List<Integer> arr = [1,2,3 ];
       
//       // Auxiliary space to store each path
//       for item : 
//       ArrayList<Integer> path = new ArrayList<>();
    
    
//       printSubsequences(arr, 0, path);
//       System.out.println(sum);
    
// }
// }