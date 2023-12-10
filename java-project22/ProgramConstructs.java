import java.util.HashMap;

public class ProgramConstructs {
    
    public static void main(String[] args) {

        // Delcaring an Array
        int[] myArray = new int[5];
        // OR
        int[] myArr = {12, 34, 25, 78, -90, -1, 0};
        // Printing an array
        int len = myArr.length;

            for(int i = 0; i < len; i++){
            
                System.out.println(myArr[i]);
                // we can also use this line for more detailed printing
                // System.out.println("Index "+i+" Value "+ myAarr[i]);
        }
        // Operating on an array
        // Adding 12 to an element if they are at even index
        // Multiplying by 2 if they are at odd index
        for(int i = 0; i<len; i++){

            // check the index value
            if( i%2 == 0)
            myArr[i] = myArr[i] + 12;
            else
            myArr[i] = myArr[i]*2;
        }

        //====================================Strings=======================================

        // Declaration
        String name = "ATLAS";
        len = name.length();
        
        // Print a String
        System.out.println(name);

        //Acces a letter (character of a string)
        // word =  ATLAS
        // index = 01234

        char letter = name.charAt(2); // gives L
        
        // Printing characters/letters of a string sepearately and storing them in an array 
        char[] letters = new char[len];
        
        for(int i = 0; i < len; i++){

            char ch = name.charAt(i);
            letters[i] = ch;
        }
        // to print the array we use the same code as above 
        for(int i = 0; i < len; i++){
            
                System.out.println(letters[i]);
                // we can also use this line for more detailed printing
                // System.out.println("Index "+i+" Value "+ myAarr[i]);
        }

        //============================HashMap=================================
        
        //   KEY  |  VALUE
        //   34   |  "even"
                
        // we use import java.util.HashMap or Map
        // Examples 
        // HashMap<Integer, Double> numbers = new HashMap<Integer, Double>();
        // HashMap<Integer, Float> numbers = new HashMap<Integer, Float>();
        // HashMap<String, Integer> numbers = new HashMap<String, Integer>();

        HashMap<Integer, String> numbers = new HashMap<Integer, String>();

        // Add keys and values (number, "type")
        // To input or make new entry in the table we use put() function
        numbers.put(45, "Odd");
        numbers.put(34, "Even");
        numbers.put(12, "Even");
        numbers.put(67, "Odd");

        // Print the map
        System.out.println(numbers);

        // To get the Value of a Key from map we use - get() function
        // Since the Value had a type String we store it in a String type.
        String value = numbers.get(45);
        System.out.println(value);

        // To check if a Key exists in the map or not we use containsKey() function
        // return - True (key exists), False - (key does not exist)
        boolean isPresent = numbers.containsKey(67);
        System.out.println("67 present? "+isPresent);

        isPresent = numbers.containsKey(94);
        System.out.println("94 present? "+isPresent);

        HashMap<Integer, Integer> items = new HashMap<>();
        int[] arr = {12, 34, 12, 35, 2, 3, 5, 34, 12, 90, 90};
        for(int i =0; i<arr.length; i++){

            if(items.containsKey(arr[i])){
                items.put( arr[i], items.get(arr[i]) + 1);
            }else{
                items.put(arr[i], 1);
            }
        }
        System.out.println("Items "+items);



    }

}
