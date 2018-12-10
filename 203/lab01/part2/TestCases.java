import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.lang.reflect.Field;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;

public class TestCases
{

   public static final double DELTA = 0.00001;

   /*
    * This test is just to get you started.
    */
   @Test
   public void testGetX()
   {
      assertEquals(1.0, new Point(1.0, 2.0).getX(), DELTA);
      assertEquals(3.5, new Point(3.5, 2.0).getX(), DELTA);
   }

   @Test
   public void testgetY2(){
      assertEquals(35.7, new Point(23.2, 35.7).getY(), DELTA);
      assertEquals(5.5, new Point(4.0, 5.5).getY(), DELTA);
   }

   @Test
   public void testradius(){
      assertEquals(13.0, new Point(5.0, 12.0).getRadius(), DELTA);
      assertEquals(5.0, new Point(3.0, 4.0).getRadius(), DELTA);
      assertEquals(41.0, new Point(40.0, 9.0).getRadius(), DELTA);
   }

   @Test
   public void testangle(){
      assertEquals(0.7853981633, new Point(1.0, 1.0).getAngle(), DELTA);
      assertEquals(1.57079632679, new Point(0.0, 1.0).getAngle(), DELTA);
      assertEquals(0.0, new Point(1.0, 0.0).getAngle(), DELTA);
   }


   @Test
   public void testrotate(){
      Point point1 = new Point(1.0, 1.0).rotate90();
      Point point2 = new Point(-1.0, 1.0);
      Point point3 = new Point(3.0, 5.0).rotate90();
      Point point4 = new Point(-5.0, 3.0);

      assertEquals(point1.getX(), point2.getX(), DELTA);

      
      assertEquals(point1.getY(), point2.getY(), DELTA);
      assertEquals(point3.getX(), point4.getX(), DELTA);
      assertEquals(point3.getY(), point4.getY(), DELTA); 

      /*assertEquals(point2, point1.rotate90());

      assertEquals(point4, point3.rotate90()); */
   }
   /*
    * The tests below here are to verify the basic requirements regarding
    * the "design" of your class.  These are to remain unchanged.
    */

   @Test
   public void testImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getX",
         "getY",
         "getRadius",
         "getAngle",
         "rotate90"
         );

      final List<Class> expectedMethodReturns = Arrays.asList(
         double.class,
         double.class,
         double.class,
         double.class,
         Point.class
         );

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0],
         new Class[0],
         new Class[0],
         new Class[0],
         new Class[0]
         );

      verifyImplSpecifics(Point.class, expectedMethodNames,
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

      // verify that fields are final
      final List<Field> nonFinalFields = Arrays.stream(
         clazz.getDeclaredFields())
            .filter(f -> !Modifier.isFinal(f.getModifiers()))
            .collect(Collectors.toList());

      assertEquals("Unexpected non-final fields", 0, nonFinalFields.size());
   }










}
