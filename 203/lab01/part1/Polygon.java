import java.util.Arrays;
import java.util.List;



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
}
