import java.util.ArrayList;
import java.util.List;
public class Recursion_Problems {
    public static void findCombination2(int ind, int[] input, int target, List<List<Integer>> ans, ArrayList<Integer> arr)
    {
        if(target == 0){
            ans.add(new ArrayList<>(arr));
            return;
        }
        for(int i=ind; i<input.length; i++){
            if(i>ind && input[i] == input[i-1]) continue;
            if(input[i]>target) break;

            arr.add(input[i]);
            findCombination2(i+1, input, target - input[i], ans, arr);
            arr.remove(arr.size()-1);
        }
    }
    public static void findCombination(int ind, int[] arr, int target, List<List<Integer>> ans, ArrayList<Integer> ds )
    {
        if (ind == arr.length)
        {
            if(target == 0)
            ans.add(new ArrayList<>(ds));
            return;
        }
        if(arr[ind] <= target)
        {
            ds.add(arr[ind]);
            findCombination(ind, arr, target-arr[ind], ans, ds);
            ds.remove(ds.size()-1);
        }
        findCombination(ind+1, arr, target, ans , ds);
    }
    public static void main(String[] args) {
        System.out.println("Combination Sum-1");
        int arr[] = {2,3,6,7};
        int target = 7;
        List<List<Integer>> ans = new ArrayList<>();
        findCombination2(0, arr, target, ans, new ArrayList<Integer>());
        System.out.println(ans);
    }
}
