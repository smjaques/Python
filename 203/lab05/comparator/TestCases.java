import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.Comparator;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

import org.junit.Test;
import org.junit.Before;

public class TestCases
{
   private static final Song[] songs = new Song[] {
         new Song("Decemberists", "The Mariner's Revenge Song", 2005),
         new Song("Rogue Wave", "Love's Lost Guarantee", 2005),
         new Song("Avett Brothers", "Talk on Indolence", 2006),
         new Song("Gerry Rafferty", "Baker Street", 1998),
         new Song("City and Colour", "Sleeping Sickness", 2007),
         new Song("Foo Fighters", "Baker Street", 1997),
         new Song("Queen", "Bohemian Rhapsody", 1975),
         new Song("Gerry Rafferty", "Baker Street", 1978)
      };

   @Test
   public void testArtistComparator()
   {
      assertTrue(new ArtistComparator().compare(songs[0], songs[1])<0);
   }

   @Test
   public void testLambdaTitleComparator()
   {
      Comparator<Song> TitleComp = ((Song s1, Song s2)-> 
      {return s1.getTitle().compareTo(s2.getTitle());});

      assertTrue(TitleComp.compare(songs[0], songs[1])>0);
   }

   @Test
   public void testYearExtractorComparator()
   {
      Comparator<Integer> KeyComp = ((Integer k1, Integer k2)->
      {return k2.compareTo(k1);});

      Comparator<Song> YearComp = Comparator.comparing(Song::getYear, KeyComp);

      assertTrue(YearComp.compare(songs[1], songs[2])>0);
   }

   @Test
   public void testComposedComparator()
   {
      Comparator<Song> c1 = new ArtistComparator();
      Comparator<Song> c2 = ((Song s1, Song s2)->
      {return s1.getYear() - (s2.getYear());}); 
      assertTrue(new ComposedComparator(c1, c2).compare(songs[3], songs[7])>0);
   }

   @Test
   public void testThenComparing()
   {
      Comparator<Song> TitleComp = ((Song s1, Song s2)->
      {return s1.getTitle().compareTo(s2.getTitle());});
      Comparator<Song> ArtistComp = ((Song s1, Song s2)->
      {return s1.getArtist().compareTo(s2.getArtist());});

      Comparator<Song> thenComp = TitleComp.thenComparing(ArtistComp);

      assertTrue(thenComp.compare(songs[3], songs[5])>0);
   }

   @Test
   public void runSort()
   {
      List<Song> songList = new ArrayList<>(Arrays.asList(songs));
      List<Song> expectedList = Arrays.asList(
         new Song("Avett Brothers", "Talk on Indolence", 2006),
         new Song("City and Colour", "Sleeping Sickness", 2007),
         new Song("Decemberists", "The Mariner's Revenge Song", 2005),
         new Song("Foo Fighters", "Baker Street", 1997),
         new Song("Gerry Rafferty", "Baker Street", 1978),
         new Song("Gerry Rafferty", "Baker Street", 1998),
         new Song("Queen", "Bohemian Rhapsody", 1975),
         new Song("Rogue Wave", "Love's Lost Guarantee", 2005)
         );

      Comparator<Song> TitleComp = ((Song s1, Song s2)->
      {return s1.getTitle().compareTo(s2.getTitle());});
      Comparator<Song> ArtistComp = ((Song s1, Song s2)->
      {return s1.getArtist().compareTo(s2.getArtist());});
      Comparator<Song> YearComp = ((Song s1, Song s2)->
      {return s1.getYear() - (s2.getYear());});

      songList.sort(
      ArtistComp.thenComparing(TitleComp).thenComparing(YearComp)
      );

      assertEquals(songList, expectedList);
   }
}
