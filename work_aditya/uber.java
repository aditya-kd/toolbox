// import java.util.Collection;
// import java.util.Comparator;
// import java.util.List;
// import java.util.ArrayList;
// import java.util.Arrays;

// class Uber{
//     //merge intervals 
//     public int solve(int coordinates[][])
//     {
//         int rangesum=0;
//         // Arrays.sort(coordinates, (a,b)=>Integer.compare(a[0]-b[0]));
//         Arrays.sort(coordinates, new Comparator<Integer> (){
//             public int compare(Integer a, Integer b)
//             {
//                 return b.compareTo(a);
//             }
//         });
//         List<int[]> mergedCoordinates = new ArrayList<>();
//         int start = coordinates[0][0];
//         int end = coordinates[0][1];

//         for(int i=1;i<coordinates.length;i++)
//         {
//             int currStart = coordinates[i][0];
//             int currEnd = coordinates[i][1];
//             if(currStart <= end)
//             {
//                 end = Math.max(currEnd, end);
//             }
//             else
//             {
//                 mergedCoordinates.add(new int[] {start, end});
//                 start = currEnd;
//                 end = currEnd;
//             }
//         }
//         mergedCoordinates.add(new int[] {start, end});
//         for(int range[] : mergedCoordinates)
//         {
//             rangesum+= (range[1]-range[0] +1);
//         }

//         return rangesum;
//     }
// }