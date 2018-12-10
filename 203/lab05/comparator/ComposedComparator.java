import java.util.Comparator;

public class ComposedComparator implements Comparator<Song> {
   private Comparator<Song> c1;
   private Comparator<Song> c2;
   public ComposedComparator(Comparator<Song> C1, Comparator<Song> C2) {
      this.c1 = C1;
      this.c2 = C2;
   }

   public int compare(Song s1, Song s2) {
      int check1 = c1.compare(s1, s2);
      if (check1 == 0){
         return c2.compare(s1, s2);
      }
      return check1;
   }
}
