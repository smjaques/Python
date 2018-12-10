/*
Name:  SYDNEY JAQUES
Section:  05
*/
public class Lab00
{
   public static void main(String[] args)
   {

    /* declaring and initializing some variables */
    int x = 5;
    String y = new String("hello");
    double z = 9.8;

    /* printing the variables */
    System.out.println("x: "+ x+ " y: "+ y+ " z: "+ z); 

    int[] nums = {3, 6, -1, 2};
    int size = nums.length;
    for(int num = 0; num < size; num++){
    	System.out.println(nums[num]);
    }


    /* call a function */
    int numFound = char_count(y, "l");
    System.out.println("Found: "+numFound);



    /* a counting for a loop */
    for (int i = 1; i < 11; i ++){
        System.out.print(i+" ");
    }

    System.out.println();


    }


    /* function char.count() */
    public static int char_count(String s, String c){
    	int count = 0;
    	for (int ch = 0; ch < s.length(); ch ++){
            char to_char = c.charAt(0);
            char comparison = s.charAt(ch);

            if(to_char == comparison){
				count ++;
			}  
		}
		return count;
    }
    

}







   
   

