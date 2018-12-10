import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;


public class driver{
   public static void main(String[] args){

      List<Point> points = new ArrayList<Point>();
      points.add(new Point(0.0, 0.0));
      points.add(new Point(3.0, 1.0));
      points.add(new Point(1.0, 4.0));
      points.add(new Point(-1.0, 4.0));
      Polygon polygon = new Polygon(points);

      double perimeter = Util.perimeter(polygon);
      System.out.print("The perimeter of this polygon is: %d"+perimeter);
   }
}