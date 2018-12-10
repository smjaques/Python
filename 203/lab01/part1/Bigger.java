public class Bigger{

	/* Static Method */ 
	public static double whichIsBigger(Circle circle, Rectangle rectangle, Polygon polygon){
		Util perm = new Util();
		double circ_perimeter = perm.perimeter(circle);
		double rect_perimeter = perm.perimeter(rectangle);
		double poly_perimeter = perm.perimeter(polygon);

		if ((circ_perimeter > rect_perimeter) && (circ_perimeter > poly_perimeter)){
			return circ_perimeter;
		}
		else if((rect_perimeter > circ_perimeter) && (rect_perimeter > poly_perimeter)){
			return rect_perimeter;
		}

		return poly_perimeter;


		}
		
	}