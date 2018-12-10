import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;


public class Polygon{
	// Instance Variables
	private final List<Point> points;

	// Constrictors //
	public Polygon(List<Point> points){
		this.points = points;
	}

	// Getter Methods //
	public List getPoints(){
		return points;
	}

	public double perimeter(){
		List<Point> pts = this.getPoints();
		double perimeter = 0.0;
		for (int i = 0; i< pts.size()-1; i++){
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
