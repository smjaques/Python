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
		double perimeter = 0.0;
		int size = ((pts.size()) - 1);
		for(int i = 0; i < size; i++){
			double x1 = pts.get(i).getX();
			double x2 = pts.get(i+1).getX();
			double y1 = pts.get(i).getY();
			double y2 = pts.get(i+1).getY();
			double distance = Math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)));
			perimeter = perimeter + distance;
		}

		int last_index = pts.size() - 1;
		double x_final = pts.get(last_index).getX();
		double x_first = pts.get(0).getX();
		double y_final = pts.get(last_index).getY();
		double y_first = pts.get(0).getY();
		double last_distance = Math.sqrt(((x_final - x_first) * (x_final - x_first)) + ((y_final - y_first) * (y_final - y_first)));
		perimeter = perimeter + last_distance;
		return perimeter;
		
	}













































}

