import java.awt.Color;
import java.awt.Point;
import java.util.List;

public class Circle
   implements Shape {
   private Point center;
   private double radius;
   private Color color;

   public Circle(double Radius, Point Center, Color Color) {
      this.radius = Radius;
      this.center = Center;
      this.color = Color;
   }
   
   public Point getCenter() { return center; }
   public double getRadius() { return radius; }
   public void setRadius(double r) {
      this.radius = r;
   }
   public Color getColor() { return color; }
   public void setColor(Color c) {
      this.color = c;
   }
   public double getArea() {
      double area = Math.PI * radius * radius;
      return area;
   }
   public double getPerimeter() {
      double perimeter = 2 * Math.PI * radius;
      return perimeter;
   }
   public void translate(Point a) {
      double newx = center.getX() + a.getX();
      double newy = center.getY() + a.getY();
      center = new Point((int)newx, (int)newy);
   }
}
