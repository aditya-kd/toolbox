
class BubbleSort {

    public static void main(String args[]) {
      
    int[] data = { -2, 45, 0, 11, -9 };
    
    System.out.println("Before Sorting");
    display(data);
    // call method to sort and passing data array
    bubbleSort(data);
    System.out.println("After Sorting");
    display(data);

  }

   public static void display(int[] arr) {
        int len = arr.length;

        for(int i = 0; i < len; i++){
            
            System.out.println(arr[i]);
            // we can also use line below for more detailed printing
            // System.out.println("Index "+i+" Value "+ arr[i]);
        }
    }

  // perform the bubble sort in a separate function
  static void bubbleSort(int array[]) {
    int size = array.length;
    
    // loop to access each array element
    for (int i = 0; i < size - 1; i++)
    
      // loop to compare array elements
      for (int j = 0; j < size - i - 1; j++)

        // compare two adjacent elements
        // change > to < to sort in descending order
        if (array[j] > array[j + 1]) {

          // swapping occurs if elements
          // are not in the intended order
          int temp = array[j];
          array[j] = array[j + 1];
          array[j + 1] = temp;
        }
  }
}