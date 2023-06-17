import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//import java.io.*;

public class Inputs{
    public static void display(int[] arr, int n){
        for (int i=0; i<n; i++){

            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) throws IOException{
        
        // Declaring input object
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Variable declaration
        String word;
        String sentence;
        int age;
        int[] arr = new int[5];
        float fnum;
        double dnum;
        char ch;
        
        // Performing inputs
        word = br.readLine();
        sentence = br.readLine();
        age = Integer.parseInt(br.readLine());
        fnum = Float.parseFloat(br.readLine());
        dnum = Double.parseDouble(br.readLine());
        
        // Character Input
        ch = br.readLine().charAt(0);
        
        // Array Input
        int size = 5;
        String[] input = br.readLine().split(" ");
        for(int i=0;i<size;i++){
            
            arr[i] = Integer.parseInt(input[i]);
        }
        
        // Display 
        System.out.println("This is the output: ");
        System.out.println("Word: "+word);
        System.out.println("Sentence: "+sentence);
        System.out.println("Integer: "+age);
        System.out.println("Float: "+fnum);
        System.out.println("Doable: "+dnum);
        System.out.println("Character: "+ch);

        System.out.println("Array: ");
        display(arr, size);
        
    }
}