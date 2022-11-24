import java.util.ArrayList;
import java.util.List;

class Recursion_ReverseArr{
    // Return the reverse of a string
    public static int[] reverse(int[] arr, int i, int j){
        if ( i>=arr.length/2){
            return arr;
        }
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        return reverse(arr, i+1, j-1);
    }
    // Check whether a string is palindrome or not
    public static boolean isPalindrome(String str, int i, int j){
        if( i >= j){
            return true;
        }
        if (str.charAt(i) != str.charAt(j)){
            return false;
        }
        return isPalindrome(str, i+1, j-1);

    }
    // printing the nth Fibonacci Number
    public static int fibo(int n){
        if (n ==  1) return 0;
        if (n == 2 || n == 3 ) return 1;
        
        return fibo(n-1) + fibo(n-2);
    }// printing the fibonacci series
    public static void printFibo(int n){
            for(int i =1;i<n+1;i++){
                System.out.print(fibo(i)+" ");
            }
            System.out.println();
    }
    // printing the subsequences 
    public static void subsequences(int ind, int n, List<Integer> arr, List<Integer> input){
        
        if (ind > n){
            printList(arr);
            System.out.println();
            return;
        }
        arr.add(input.get(ind));
        subsequences(ind+1, n, arr, input);
        arr.remove(input.get(ind));
        subsequences(ind+1, n, arr, input);
    }
    // Printing the sum of all subsequences
    public static void subSum(int ind, int n, List<Integer> ds, List<Integer> input, int sum){
        if (ind > n){
            printList(ds);
            System.out.print(" Sum: "+sum);
            System.out.println();
            return;
        }
        ds.add(input.get(ind));
        sum += input.get(ind);
        subSum(ind+1, n, ds, input, sum);
        ds.remove(input.get(ind));
        sum -= input.get(ind);
        subSum(ind+1, n, ds, input, sum);
    }
    // Print if there is a subset with sum s
    public static void subSum2(int ind, int n, List<Integer> ds, List<Integer> input, int sum, int target){
        if (ind > n){
            if (sum == target){
            printList(ds);
            System.out.print(" Sum: "+sum);
            System.out.println();}
            return;
        }
        ds.add(input.get(ind));
        sum += input.get(ind);
        subSum2(ind+1, n, ds, input, sum, target);
        ds.remove(input.get(ind));
        sum -= input.get(ind);
        subSum2(ind+1, n, ds, input, sum, target);
    }
    // Functional Approach
    public static boolean subsetSumTarget(int ind, int n, List<Integer> arr, List<Integer> input, int sum, int target)
    {
        if (ind > n)
        {
            if (sum == target){
                return true;
            }
            else return false;
        }
        arr.add(input.get(ind));
        sum += input.get(ind);

        if ( subsetSumTarget(ind+1, n, arr, input, sum, target) == true)
        { return true;}

        arr.remove(input.get(ind));
        sum -= input.get(ind);

        if( subsetSumTarget(ind+1, n, arr, input, sum, target) == true)
        return true;

        return false;
    }
    // count the subsequences with sum k
    public static int countSubsetSumK(int ind, int n, List<Integer> arr, List<Integer> input, int sum, int target, int count)
    {
        if (ind > n)
        {
            if (sum == target){
                printList(arr);System.out.println();
                count++;
                return count;}
            else 
            return count;
        }
        arr.add(input.get(ind));
        sum += input.get(ind);

        int res1 = countSubsetSumK(ind+1, n, arr, input, sum, target,count);
        
        arr.remove(input.get(ind));
        sum -= input.get(ind);

        int res2 = countSubsetSumK(ind+1, n, arr, input, sum, target, count);
        return res1 + res2;
    }
    public static int countSubsetSumTarget(int ind, int n, List<Integer> arr, List<Integer> input, int sum, int target, int count)
    {
        if(ind > n){
            if (sum == target)
            {
                count++;
                return count;
            }
            else  return count;
        }
        arr.add(input.get(ind));
        sum += input.get(ind);

        int res1 = countSubsetSumTarget(ind+1, n, arr, input, sum, target, count);
      
        arr.remove(input.get(ind));
        sum -= input.get(ind);
        int res2 = countSubsetSumTarget(ind+1, n, arr, input, sum, target, count);

        return res1 + res2;
    }
    public static void printList(List<Integer> arr){
        System.out.print(arr);
    }
    public static void printArr(int[] arr){
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] arr = {5,4,3,1};
        String str = "racecar";
        int n = arr.length;
        System.out.println("Reverse of Arr");
        int[] rev = reverse(arr, 0, n-1);
        printArr(rev);
        System.out.println(isPalindrome(str, 0, str.length()-1));
        System.out.println("Printing Fibonacci Series:");
        printFibo(10);
        List<Integer> arr2 = new ArrayList<Integer>();
        List<Integer> input = new ArrayList<Integer>();
        input.add(3);
        input.add(1);
        input.add(2);
        input.add(5);
        System.out.println("Printing the subequences");
        subsequences(0, input.size()-1, arr2, input);
        System.out.println("Printing the sum of subesequences");
        int target = 5;
        subSum2(0, input.size()-1, arr2, input, 0, target);
        System.out.println("Check if a subset exists with sum: "+target);
        System.out.println(subsetSumTarget(0, input.size()-1, arr2, input, 0, target));
        System.out.println("Counting the subset with sum "+target);
        System.out.println(countSubsetSumK(0, input.size()-1, arr2, input, 0, target, 0));
        System.out.println(countSubsetSumTarget(0, input.size()-1, arr2, input, 0, target, 0));

    }

}