import java.io.*;

public class SortsRunner {
    public static void main(String[] args){
        try {
            BufferedReader reader = new BufferedReader(new FileReader(args[0]));
            String array = reader.readLine();
            System.out.println(array);
        } catch (Exception FileNotFoundException) {
            System.out.println("Error: File Not Found");
            return;
        }
        Sorts sorts = new Sorts();
        sorts.selectionSort();
        sorts.InsertionSort();
        sorts.MergeSort();


    }
}
