class SimpleLoop
{
   public static int sum(int low, int high)
   {
   	int count = 0;
   	for(int i=low; i<=high; i++){
   		count = count + i;
   	}


      /* TO DO:  Return the sum of the integers between
         low and high (inclusive).  Yes, this can be
         done without a loop, but the point is to
         practice the syntax for a loop.
      */

      return count;
   }
}
