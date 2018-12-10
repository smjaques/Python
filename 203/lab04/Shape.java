import java.awt.Color;
import java.awt.Point;

interface Shape {
   Color getColor();
   void setColor(Color c);
   double getArea();
   double getPerimeter();
   void translate(Point a);
}
