public class QuickSort {
    
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for(int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i = i + 1;
                // swap elements at i and j index
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // choosing the element at high and swap with i+1 index to make it the pivot.
        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;

        // new pivot is now at i+1, so we return it.
        return i+1; 
    }

    public static void quickSort(int[] arr, int low, int high){
        
        if(low < high) {
            // get the pivot element.
            int p = partition(arr, low, high);
            // sort elements before pivot
            quickSort(arr, low, p-1);
            //sort elements after pivot
            quickSort(arr, p+1, high);
        }
    }

    public static void display(int[] arr) {
        int len = arr.length;

        for(int i = 0; i < len; i++){
            
            System.out.println(arr[i]);
            // we can also use this line for more detailed printing
            // System.out.println("Index "+i+" Value "+ arr[i]);
        }
    }
    public static void main(String[] args) {
        
        int[] arr = {78, -90, 45, 23, 34, 11, 12};
        int len = arr.length;
        
        // Print before sorting 
        System.out.println("Array before Sorting");
        display(arr);
        // Call the Quick Sort function and pass the array
        quickSort(arr, 0, len-1);

        System.out.println("Array after sorting");
        display(arr);
    }
}
