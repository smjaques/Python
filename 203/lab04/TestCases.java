import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

import java.awt.Color;
import java.awt.Point;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;
import org.junit.Test;

public class TestCases
{
   public static final double DELTA = 0.00001;

   /* some sample tests but you must write more! see lab write up */

   @Test
   public void testCircleGetArea()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(101.2839543, c.getArea(), DELTA);
   }

   @Test
   public void testCircleGetPerimeter()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);

      assertEquals(35.6759261, c.getPerimeter(), DELTA);
   }

   @Test
   public void testCircleTranslate()
   {
      Circle c = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Point p = new Point(8, 8);
      c.translate(p);
      assertEquals(new Point(10,11), c.getCenter());
   }

   @Test
   public void testCircleGetColor()
   {
      Circle c = new Circle(3.2, new Point(2, 3), Color.BLACK);
      assertEquals(Color.BLACK, c.getColor());
   }

   @Test
   public void testCirlceGetColor2()
   {
      Circle c = new Circle(3.2, new Point(2, 3), Color.PINK);
      assertEquals(Color.PINK, c.getColor());
   }

   @Test
   public void testCircleGetCenter()
   {
      Circle c = new Circle(3.2, new Point(2, 3), Color.PINK);
      assertEquals(new Point(2, 3), c.getCenter());

   }

   @Test
   public void testRectangleGetArea()
   {
      Rectangle r = new Rectangle(1.0, 2.0, new Point(8,8), Color.BLUE);
      assertEquals(2.0, r.getArea(), DELTA);
   }
   
   @Test
   public void testRectangleGetPerimeter()
   {
      Rectangle r = new Rectangle(1.0, 2.0, new Point(8,8), Color.BLUE);
      assertEquals(6.0, r.getPerimeter(), DELTA);
   }

   @Test
   public void testRectangleTranslate()
   {
      Rectangle r = new Rectangle(1.0, 2.0, new Point(8,8), Color.BLUE);
      Point p = new Point(3,3);
      r.translate(p);
      assertEquals(new Point(11,11), r.getTopLeft());
   }


   @Test
   public void testTriangleGetArea()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.RED);
      assertEquals(6.5, t.getArea(), DELTA);
   }

   @Test
   public void testTriangleGetPerimeter()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.RED);
      assertEquals(17.851139534682794, t.getPerimeter(), DELTA);
   }

   @Test
   public void testTriangleGetVertexA()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.RED);
      assertEquals(new Point(1, 1), t.getVertexa());  
   }

   @Test
   public void testTriangleGetVertexB()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.RED);
      assertEquals(new Point(2, 8), t.getVertexb());  
   }

   @Test
   public void testTriangleGetColor()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.RED);
      assertEquals(Color.RED, t.getColor());
   }

   @Test
   public void testTriangleGetColor2()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.BLACK);
      assertEquals(Color.BLACK, t.getColor());
   }

   @Test
   public void testTriangleTranslate()
   {
      Triangle t = new Triangle(new Point(1,1), new Point(2,8), new Point(4,9), Color.RED);
      Point p = new Point(1,1);
      t.translate(p);
      assertEquals(new Point(2,2), t.getVertexa());
      assertEquals(new Point(3,9), t.getVertexb());
      assertEquals(new Point(5,10), t.getVertexc());
      //assertEquals(a, t);
   }

   @Test
   public void testPolygonGetArea()
   {
      Point vertices[] = new Point[5];
      vertices[0] = new Point(1,1);
      vertices[1] = new Point(3,3);
      vertices[2] = new Point(8,8);
      vertices[3] = new Point(10,10);
      vertices[4] = new Point(11,11);
      ConvexPolygon poly = new ConvexPolygon(vertices, Color.GREEN);
      assertEquals(0, poly.getArea(), DELTA);
   }

   @Test
   public void testPolygonGetPerimeter()
   {
      Point vertices[] = new Point[5];
      vertices[0] = new Point(1,1);
      vertices[1] = new Point(3,3);
      vertices[2] = new Point(8,8);
      vertices[3] = new Point(10,10);
      vertices[4] = new Point(11,11);
      ConvexPolygon poly = new ConvexPolygon(vertices, Color.GREEN);
      assertEquals(28.284271247461902, poly.getPerimeter(), DELTA);
   }

   @Test
   public void testPolygonGetColor()
   {
      Point vertices[] = new Point[5];
      vertices[0] = new Point(1,1);
      vertices[1] = new Point(3,3);
      vertices[2] = new Point(8,8);
      vertices[3] = new Point(10,10);
      vertices[4] = new Point(11,11);
      ConvexPolygon poly = new ConvexPolygon(vertices, Color.GREEN);  
      assertEquals(Color.GREEN, poly.getColor());
   }

   @Test
   public void testPolygonTranslate()
   {
      Point vertices[] = new Point[5];
      vertices[0] = new Point(1,1);
      vertices[1] = new Point(3,3);
      vertices[2] = new Point(8,8);
      vertices[3] = new Point(10,10);
      vertices[4] = new Point(11,11);
      Point vertices2[] = new Point[5];
      vertices2[0] = new Point(2,2);
      vertices2[1] = new Point(4,4);
      vertices2[2] = new Point(9,9);
      vertices2[3] = new Point(11,11);
      vertices2[4] = new Point(12,12);
      Point p = new Point(1,1);
      ConvexPolygon poly = new ConvexPolygon(vertices, Color.GREEN);
      ConvexPolygon poly2 = new ConvexPolygon(vertices2, Color.GREEN);
      poly.translate(p);
      assertEquals(poly2.getVertex(0), poly.getVertex(0));
      assertEquals(poly2.getVertex(1), poly.getVertex(1));
      assertEquals(poly2.getVertex(2), poly.getVertex(2));
      assertEquals(poly2.getVertex(3), poly.getVertex(3));
      assertEquals(poly2.getVertex(4), poly.getVertex(4));
   }

   @Test
   public void testWorkSpaceAreaOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), 
                 Color.BLACK));

      assertEquals(114.2906063, ws.getAreaOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpacePerimeterOfAllShapes()
   {
      WorkSpace ws = new WorkSpace();

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Circle(5.678, new Point(2, 3), Color.BLACK));
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
                 Color.BLACK));

      assertEquals(61.09516775478293, ws.getPerimeterOfAllShapes(), DELTA);
   }

   @Test
   public void testWorkSpaceGetRectangles()
   {
      WorkSpace ws = new WorkSpace();
      List<Rectangle> expected = new LinkedList<>();
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);
      Rectangle r1 = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);
      ws.add(r1);
      ws.add(c1);
      Triangle t1 = new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), Color.BLACK);
      ws.add(t1);
      ws.add(c2);

      expected.add(r1);
      assertEquals(expected, ws.getRectangles());
   }
   
   @Test
   public void testWorkSpaceGetTriangles()
   {
      WorkSpace ws = new WorkSpace();
      List<Triangle> expected = new LinkedList<>();
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);
      Rectangle r1 = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);
      ws.add(r1);
      ws.add(c1);
      Triangle t1 = new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), Color.BLACK);
      ws.add(t1);
      ws.add(c2);

      expected.add(t1);
      assertEquals(expected, ws.getTriangles());
   }

   @Test
   public void testWorkSpaceGetCircles()
   {
      WorkSpace ws = new WorkSpace();
      List<Circle> expected = new LinkedList<>();

      // Have to make sure the same objects go into the WorkSpace as
      // into the expected List since we haven't overriden equals in Circle.
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);

      ws.add(new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK));
      ws.add(c1);
      ws.add(new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0),
                 Color.BLACK));
      ws.add(c2);

      expected.add(c1);
      expected.add(c2);

      // Doesn't matter if the "type" of lists are different (e.g Linked vs
      // Array).  List equals only looks at the objects in the List.
      assertEquals(expected, ws.getCircles());
   }

   @Test
   public void testWorkSpaceGetPolygons()
   {
      WorkSpace ws = new WorkSpace();
      List<ConvexPolygon> expected = new LinkedList<>();
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);
      Rectangle r1 = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);
      ws.add(r1);
      ws.add(c1);
      Triangle t1 = new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), Color.BLACK);
      ws.add(t1);
      ws.add(c2);
      Point vertices[] = new Point[5];
      vertices[0] = new Point(1,1);
      vertices[1] = new Point(3,3);
      vertices[2] = new Point(8,8);
      vertices[3] = new Point(10,10);
      vertices[4] = new Point(11,11);
      ConvexPolygon poly = new ConvexPolygon(vertices, Color.PINK);
      ws.add(poly);
      expected.add(poly);
      assertEquals(expected, ws.getConvexPolygons());
   }

   @Test
   public void testGetShapesByColor()
   {
      WorkSpace ws = new WorkSpace();
      List<Shape> expected = new LinkedList<>();
      Circle c1 = new Circle(5.678, new Point(2, 3), Color.BLACK);
      Circle c2 = new Circle(1.11, new Point(-5, -3), Color.RED);
      Rectangle r1 = new Rectangle(1.234, 5.678, new Point(2, 3), Color.BLACK);
      ws.add(r1);
      ws.add(c1);
      Triangle t1 = new Triangle(new Point(0,0), new Point(2,-4), new Point(3, 0), Color.BLACK);
      ws.add(t1);
      ws.add(c2);
      Point vertices[] = new Point[5];
      vertices[0] = new Point(1,1);
      vertices[1] = new Point(3,3);
      vertices[2] = new Point(8,8);
      vertices[3] = new Point(10,10);
      vertices[4] = new Point(11,11);
      ConvexPolygon poly = new ConvexPolygon(vertices, Color.PINK);
      ws.add(poly);
      expected.add(r1);
      expected.add(c1);
      expected.add(t1);
      assertEquals(expected, ws.getShapesByColor(Color.BLACK));
   }
   /* HINT - comment out implementation tests for the classes that you have not 
    * yet implemented */
   @Test
   public void testCircleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getRadius", "setRadius", "getCenter");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0]);

      verifyImplSpecifics(Circle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testRectangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getWidth", "setWidth", "getHeight", "setHeight", "getTopLeft");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         double.class, void.class, double.class, void.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[] {double.class}, new Class[0], new Class[] {double.class}, new Class[0]);

      verifyImplSpecifics(Rectangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testTriangleImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertexa", "getVertexb", "getVertexc");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class, Point.class, Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[0], new Class[0], new Class[0]);

      verifyImplSpecifics(Triangle.class, expectedMethodNames,
         expectedMethodReturns, expectedMethodParameters);
   }

   @Test
   public void testConvexPolygonImplSpecifics()
      throws NoSuchMethodException
   {
      final List<String> expectedMethodNames = Arrays.asList(
         "getColor", "setColor", "getArea", "getPerimeter", "translate",
         "getVertex");

      final List<Class> expectedMethodReturns = Arrays.asList(
         Color.class, void.class, double.class, double.class, void.class,
         Point.class);

      final List<Class[]> expectedMethodParameters = Arrays.asList(
         new Class[0], new Class[] {Color.class}, new Class[0], new Class[0], new Class[] {Point.class},
         new Class[] {int.class});

      verifyImplSpecifics(ConvexPolygon.class, expectedMethodNames,
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
         0, clazz.getFields().length);

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

}
