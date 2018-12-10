import java.awt.Color;
import java.awt.Point;
import java.util.List;

public class Triangle implements Shape {
   private Point vertexa;
   private Point vertexb;
   private Point vertexc;
   private Color color;

   public Triangle(Point VertexA, Point VertexB, Point VertexC, Color Color) {
      this.vertexa = VertexA;
      this.vertexb = VertexB;
      this.vertexc = VertexC;
      this.color = Color;
   }

   public Point getVertexa() { return vertexa; }
   public Point getVertexb() { return vertexb; }
   public Point getVertexc() { return vertexc; }
   public Color getColor() { return color; }
   public void setColor(Color c) {
      this.color = c;
   }
   public double getArea() {
      double area = (vertexa.getX() * (vertexb.getY() - vertexc.getY()) + vertexb.getX() * (vertexc.getY() - vertexa.getY()) + vertexc.getX() * (vertexa.getY() - vertexb.getY())) / 2;
      return Math.abs(area);
   }
   public double getPerimeter() {
      double side1 = Math.hypot(vertexa.getX() - vertexb.getX(), vertexa.getY() - vertexb.getY());
      double side2 = Math.hypot(vertexb.getX() - vertexc.getX(), vertexb.getY() - vertexc.getY());
      double side3 = Math.hypot(vertexc.getX() - vertexa.getX(), vertexc.getY() - vertexa.getY());
      double perimeter = side1 + side2 + side3;
      return perimeter;
   }
   public void translate(Point a) {
      double newax = vertexa.getX() + a.getX();
      double neway = vertexa.getY() + a.getY();
      double newbx = vertexb.getX() + a.getX();
      double newby = vertexb.getY() + a.getY();
      double newcx = vertexc.getX() + a.getX();
      double newcy = vertexc.getY() + a.getY();
      vertexa = new Point((int)newax, (int)neway);
      vertexb = new Point((int)newbx, (int)newby);
      vertexc = new Point((int)newcx, (int)newcy);
   }
}

