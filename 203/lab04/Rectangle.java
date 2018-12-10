import java.awt.Color;
import java.awt.Point;
import java.util.List;

public class Rectangle implements Shape {
   private double width;
   private double height;
   private Point topleft;
   private Color color;

   public Rectangle(double Width, double Height, Point TopLeft, Color Color) {
      this.width = Width;
      this.height = Height;
      this.topleft = TopLeft;
      this.color = Color;
   }

   public double getWidth() { return width; }
   public double getHeight() { return height; }
   public void setWidth(double w) {
      this.width = w;
   }
   public void setHeight(double h) {
      this.height = h;
   }
   public Color getColor() { return color; }
   public void setColor(Color c) {
      this.color = c;
   }
   public double getArea() {
      double area = width * height;
      return area;
   }
   public double getPerimeter() {
      double perimeter = 2 * width + 2 * height;
      return perimeter;
   }
   public Point getTopLeft() { return topleft; }
   public void translate(Point a) {
      double newtlx = topleft.getX() + a.getX();
      double newtly = topleft.getY() + a.getY();
      topleft = new Point((int)newtlx, (int)newtly);
   }
}

