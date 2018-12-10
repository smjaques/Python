import java.awt.Color;
import java.awt.Point;
import java.util.List;
import java.util.Arrays;

public class ConvexPolygon implements Shape{
   private Point[] vertices;
   private Color color;

   public ConvexPolygon(Point[] vertices, Color c){
      this.vertices = vertices;
      this.color = c;
   }
   public Point getVertex(int i){
      return vertices[i];
   }

   public Color getColor() {
      return color;
   }

   public void setColor(Color c){
      this.color = c;
   }

   public double getArea(){
      double area1 = 0;
      double area2 = 0;
      int size = vertices.length;
      for (int i=0; i<(size-2); i++){
         area1 +=(getVertex(i).getX() * getVertex(i+1).getY());
         area2 += (getVertex(i).getY() * getVertex(i+1).getX());
      }

      area1 += (getVertex(size-1).getX() * getVertex(0).getY());

      area2 += (getVertex(size-1).getY() * getVertex(0).getX());

      double totalarea = 0.5 * (area1 - area2);
      return totalarea;
    }

   public double getPerimeter(){
      double totalperimeter = 0;
      for (int i=0; i<(vertices.length -1); i++){
         double x1 = vertices[i].getX();
         double x2 = vertices[i+1].getX();
         double y1 = vertices[i].getY();
         double y2 = vertices[i+1].getY();
         double dist = Math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 -y2)));
         totalperimeter += dist;
      }
      int lasti = vertices.length - 1;
      double lastx = vertices[lasti].getX();
      double firstx = vertices[0].getX();
      double lasty = vertices[lasti].getY();
      double firsty = vertices[0].getY();
      double lastdist = Math.sqrt(((lastx - firstx) * (lastx - firstx)) + ((lasty - firsty) * (lasty - firsty)));
      totalperimeter += lastdist;
      return totalperimeter;
    }

    public void translate(Point a){
        for (int i=0; i<(vertices.length); i++){
            vertices[i] = new Point((int)vertices[i].getX()+(int)a.getX(),
                                (int)vertices[i].getY()+(int)a.getY());
        }
    }

}

