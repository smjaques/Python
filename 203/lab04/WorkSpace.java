import java.awt.Color;
import java.awt.Point;
import java.util.List;
import java.util.ArrayList;

public class WorkSpace {
   private List<Shape> shapes = new ArrayList<>();

   public WorkSpace() {}

   public void add(Shape shape) {
      shapes.add(shape);
   }
   public Shape get(int index) {
      return shapes.get(index);
   }
   public int size() {
      int total = 0;
      for (Shape shape : shapes) {
         total += 1;
      }
      return total;
   }
   public List<Circle> getCircles() {
      List<Circle> circles = new ArrayList<>();
      for (Shape shape : shapes) {
         if (shape instanceof Circle) {
            circles.add((Circle)shape);
         }
      }
      return circles;
   }
   public List<Rectangle> getRectangles() {
      List<Rectangle> rectangles = new ArrayList<>();
      for (Shape shape : shapes) {
         if (shape instanceof Rectangle) {
            rectangles.add((Rectangle)shape);
         }
      }
      return rectangles;
   }
   public List<Triangle> getTriangles() {
      List<Triangle> triangles = new ArrayList<>();
      for (Shape shape : shapes) {
         if (shape instanceof Triangle) {
            triangles.add((Triangle)shape);
         }
      }
      return triangles;
   }
   public List<ConvexPolygon> getConvexPolygons() {
      List<ConvexPolygon> polygons = new ArrayList<>();
      for (Shape shape : shapes) {
         if (shape instanceof ConvexPolygon) {
            polygons.add((ConvexPolygon)shape);
         }
      }
      return polygons;
   }
   public List<Shape> getShapesByColor(Color color) {
      List<Shape> coloredshapes = new ArrayList<>();
      for (Shape shape : shapes) {
         if (shape.getColor() == color) {
            coloredshapes.add(shape);
         }
      }
      return coloredshapes;
   }
   public double getAreaOfAllShapes() {
      double totalarea = 0;
      for (Shape shape : shapes) {
         double area = shape.getArea();
         totalarea += area;
      }
      return totalarea;
   }
   public double getPerimeterOfAllShapes() {
      double totalperimeter = 0;
      for (Shape shape : shapes) {
         double perimeter = shape.getPerimeter();
         totalperimeter += perimeter;
      }
      return totalperimeter;
   }

}

