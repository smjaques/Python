public class Sorts {
    public Sorts(){

    }
    public static String[] selectionSort(String[] arr){
        int n = arr.length;
        for(int i = 0; i < n-1; i++){
            int smallestI = i;
            for(int j = i+1; j < n; j++){
                if(Integer.parseInt(arr[j]) < Integer.parseInt(arr[smallestI])){
                    smallestI = j;
                }
            }
            String temp = arr[smallestI];
            arr[smallestI] = arr[i];
            arr[i] = temp;
        }
        return arr;
    }

    public static String[] insertionSort(String[] arr){
        int n = arr.length;
        for(int i = 1; i < n; i ++){
            String curr = arr[i];
            int k = i - 1;
            //shifting value down list while greater than
            while(k>=0 && Integer.parseInt(arr[k]) > Integer.parseInt(curr)){
                arr[k+1] = arr[k];
                k = k-1;
            }
            arr[k+1] = curr;
        }
        return arr;
    }

    public static String[] merge(String[] arr, String[] firstHalf, String[] secondHalf){
        int i = 0;
        int j = 0;
        int k = 0;

        while(i < firstHalf.length && j < secondHalf.length){
            if(Integer.parseInt(firstHalf[i]) < Integer.parseInt(secondHalf[j])){
                arr[k] = firstHalf[i];
                i++;
            }
            else{
                arr[k] = secondHalf[j];
                j++;
            }
            k++;
        }

        //none left of firstHalf, all secondHalf remaining
        while(j < secondHalf.length){
            arr[k] = secondHalf[j];
            j++;
            k++;
        }

        //none left of secondHalf, all firstHalf remaining
        while(i < firstHalf.length){
            arr[k] = firstHalf[i];
            i++;
            k++;
        }
        return arr;
    }

    public static String[] mergeSort(String[] arr){
        String[] finalSorted = new String[arr.length];
        if(arr.length == 0){
            return arr;
        }

        if(arr.length > 1){
            int half = arr.length / 2;

            //Split first half
            String[] firstHalf = new String[half];
            for(int i = 0; i < half; i++){
                firstHalf[i] = arr[i];
            }

            //Split second half
            String[] secondHalf = new String[arr.length-half];
            for(int i = half; i < arr.length; i++){
                secondHalf[i-half] = arr[i];
            }
            mergeSort(firstHalf);
            mergeSort(secondHalf);

            //merge the sorted arrays
            finalSorted = merge(arr, firstHalf, secondHalf);
        }
        return finalSorted;
    }
}
