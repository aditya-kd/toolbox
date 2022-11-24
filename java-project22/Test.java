import java.util.List;
import java.util.ArrayList;
public class Test {

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
public static void printSum(int ind, int n, List<Integer> arr, List<Integer> input, int sum)
{
    if (ind > n){
        System.out.println("Sum is: "+sum);
        printList(arr);
        return;
    }
    //take 
    arr.add(input.get(ind));
    sum += input.get(ind);
    //call with take
    printSum(ind+1, n, arr, input, sum);
    //not take
    arr.remove(input.get(ind));
    sum -= input.get(ind);
    //not take call
    printSum(ind+1, n, arr, input, sum);
}
public static void isTargetSum(int ind, int n, List<Integer> arr, List<Integer> input, int sum, int target)
{
    if(ind>n){
        if(sum == target)
        {
            printList(arr);
            System.out.println("Sum: "+sum);
        }
        return ;
    }
    //take
    arr.add(input.get(ind));
    sum += input.get(ind);

    isTargetSum(ind+1, n, arr, input, sum, target);
    // not take
    arr.remove(input.get(ind));
    sum -= input.get(ind);

    isTargetSum(ind+1, n, arr, input, sum, target);
}
public static void printList(List<Integer> arr){
    System.out.println(arr);
}

public static void main(String[] args) {
    //call the function here
    List<Integer> input = new ArrayList<>();
    List<Integer> arr = new ArrayList<>();
    input.add(2);
    input.add(5);
    input.add(3);
    input.add(1);
    int n = input.size() - 1;
    // printSum(0, n, arr, input, 0);
    isTargetSum(0, n, arr, input, 0, 17);
}
}
