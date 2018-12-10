import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Util{

	/* Static Perimeter Methods */
	public static double perimeter(Circle circle){
		double rad = circle.getRadius();
		return(2*Math.PI*rad);
	}

	public static double perimeter(Rectangle rectangle){
		Point left = rectangle.getTopLeft();
		double x = left.getX();
		double y = left.getY();

		Point right = rectangle.getBottomRight();
		double x2 = right.getX();
		double y2 = right.getY();

		double x_units = java.lang.Math.abs(x2-x);
		double y_units = java.lang.Math.abs(y2-y);

		return((2 * x_units) + (2 * y_units));
		
	}

	public static double perimeter(Polygon polygon){
		List<Point> pts = polygon.getPoints();
		Point p1 = pts.get(0);
		Point p2 = pts.get(1);
		Point p3 = pts.get(2);
		Point p4 = pts.get(3);

		double distX1_2 = ((p1.getX() - p2.getX()) * (p1.getX() - p2.getX()));
		double distY1_2 = ((p1.getY() - p2.getY()) * (p1.getY() - p2.getY()));
		double distXY1_2 = Math.sqrt(distX1_2 + distY1_2);

		double distX2_3 = ((p2.getX() - p3.getX()) * (p2.getX() - p3.getX()));
		double distY2_3 = ((p2.getY() - p3.getY()) * (p2.getY() - p3.getY()));
		double distXY2_3 = Math.sqrt(distX2_3 + distY2_3);

		double distX3_4 = ((p3.getX() - p4.getX()) * (p3.getX() - p4.getX()));
		double distY3_4 = ((p3.getY() - p4.getY()) * (p3.getY() - p4.getY()));
		double distXY3_4 = Math.sqrt(distX3_4 + distY3_4);

		double distX4_1 = ((p4.getX() - p1.getX()) * (p4.getX() - p1.getX()));
		double distY4_1 = ((p4.getY() - p1.getY()) * (p4.getY() - p1.getY()));
		double distXY4_1 = Math.sqrt(distX4_1 + distY4_1);

		return (distXY1_2 + distXY2_3 + distXY3_4 + distXY4_1); 
	}
}

