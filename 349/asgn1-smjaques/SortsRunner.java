import java.io.*;

public class SortsRunner {
    public static void main(String[] args){
        if(args.length == 0){
            return;
        }
        try {
            BufferedReader reader = new BufferedReader(new FileReader(args[0]));
            String array = reader.readLine();
            String[] arr = array.split(", ");

            String[] res1 = Sorts.selectionSort(arr);
            String joinedString1 = String.join(", ", res1);
            System.out.println("Selection Sort: " + joinedString1);

            String[] res2 = Sorts.insertionSort(arr);
            String joinedString2 = String.join(", ", res2);
            System.out.println("Insertion Sort: " + joinedString2);

            String[] res3 = Sorts.mergeSort(arr);
            String joinedString3 = String.join(", ", res3);
            System.out.println("Merge Sort    : " + joinedString3);

        } catch (Exception e) {

            System.out.println("Error: " + e);
            return;
        }



    }
}
