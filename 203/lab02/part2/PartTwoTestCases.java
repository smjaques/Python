import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;

public class PartTwoTestCases
{
   public static final double DELTA = 0.00001;

   @Test
   public void testCircleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getCenter", "getRadius", "perimeter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Point.class, double.class, double.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Circle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testRectangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getTopLeft", "getBottomRight", "perimeter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Point.class, Point.class, double.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Rectangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testPolygonImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getPoints", "perimeter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         List.class, double.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[0]);

      verifyImplSpecifics(Polygon.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   private static void verifyImplSpecifics(
      final Class<?> clazz,
      final List<String> expectedMethodNames,
      final List<Class> expectedMethodReturns,
      final List<Class[]> expectedMethodParameters)
      throws NoSuchMethodException
   {
      assertEquals("Unexpected number of public fields",
         0, Point.class.getFields().length);

      final List<Method> publicMethods = Arrays.stream(
         clazz.getDeclaredMethods())
            .filter(m -> Modifier.isPublic(m.getModifiers()))
            .collect(Collectors.toList());

      assertEquals("Unexpected number of public methods",
         expectedMethodNames.size(), publicMethods.size());

      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodReturns.size());
      assertTrue("Invalid test configuration",
         expectedMethodNames.size() == expectedMethodParameters.size());

      for (int i = 0; i < expectedMethodNames.size(); i++)
      {
         Method method = clazz.getDeclaredMethod(expectedMethodNames.get(i),
            expectedMethodParameters.get(i));
         assertEquals(expectedMethodReturns.get(i), method.getReturnType());
      }
   }

 @Test
   public void testPerimPoly() {
        List<Point> points = new ArrayList<Point>(); 
        points.add(new Point(0, 0));
        points.add(new Point(3,0));
        points.add(new Point(0,4));

        Polygon polygon = new Polygon(points);
        double d = polygon.perimeter();
        assertEquals(12.0, d, DELTA);
   }

   @Test
   public void testPerimCircle(){
      Point center = new Point(0.0, 0.0);
      Circle circle = new Circle(center, 2.0);
      assertEquals((4*Math.PI), circle.perimeter(), DELTA);
   }

   @Test
   public void testPerimCircle2(){
      Point center = new Point(1.0, 8.0);
      Circle circle = new Circle(center, 3.0);
      assertEquals((6*Math.PI), circle.perimeter(), DELTA);
   }

   @Test
   public void testPerimRect(){
      Point left = new Point(0.0, 4.0);
      Point right = new Point(4.0, 0.0);
      Rectangle rectangle = new Rectangle(left, right);
      assertEquals((16), rectangle.perimeter(), DELTA);
   }

   @Test
   public void testBigger(){
      Point center = new Point(1.0, 1.0);
      Circle circle = new Circle(center, 2.0); //4pi

      Point left = new Point(-1.0, 2.0);
      Point right = new Point(1.0, -1.6);
      Rectangle rectangle = new Rectangle(left, right); //11.2

      List<Point> points = new ArrayList<Point>();
      points.add(new Point(0.0, 0.0));
      points.add(new Point(3.0, 1.0));
      points.add(new Point(1.0, 4.0));
      points.add(new Point(-1.0, 4.0));
      Polygon polygon = new Polygon(points); //12.890934561250031

      assertEquals((12.890934561250031), Bigger.whichIsBigger(circle, rectangle, polygon), DELTA);
   }
}
