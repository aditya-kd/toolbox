public class MergeSort {
    public static void main(String[] args) {
        int[] arr = {78, -90, 45, 23, 34, 11, 12};
        int len = arr.length;
        
        // Print before sorting 
        System.out.println("Array before Sorting");
        display(arr);
        // Call the Quick Sort function and pass the array
        mergeSort(arr, 0, len-1);

        System.out.println("Array after sorting");
        display(arr);
    }
    public static void display(int[] arr) {
        int len = arr.length;

        for(int i = 0; i < len; i++){
            
            System.out.println(arr[i]);
            // we can also use this line for more detailed printing
            // System.out.println("Index "+i+" Value "+ arr[i]);
        }
    }

    public static void merge(int[] arr, int low, int mid, int high)  {

        // size of left and right arrays
        int n1 = mid - low +1;
        int n2 = high - mid;
        int i,j,k;

        int[] left = new int[n1];
        int[] right = new int[n2];

        // fill the right and left array with half elements each
        for( i = 0; i<n1; i++){

            left[i] = arr[low + i];
        }
        for( j = 0; j<n2; j++){

            right[j] = arr[mid + j + 1];
        }
        
        // reset the variables
        i = 0;
        j = 0;
        k = low;
        
        // start filling the original array arr in sorted order
        while( i < n1 && j < n2) {
            
            //check for the smaller element
            if( left[i] < right[j]){
                
                arr[k] = left[i];
                i = i+1; // or i += 1

            }else {
                arr[k] = right[j];
                j = j+1; // or j += 1 
            }
            k += 1;
        }
        // Fill the remaining elements
        while( i < n1){

            arr[k] = left[i];
            i += 1;
            k += 1;
        }
        while( j < n2){

            arr[k] = right[j];
            j += 1;
            k +=1 ;
        }
    }
    
    public static void mergeSort(int[] arr, int low, int right) {
        if( low < right) {

            int mid = low + (right - low)/2;
            mergeSort(arr, low, mid);
            mergeSort(arr, mid+1, right);
            merge(arr, low, mid, right);
        }
    }
}
