public class Rectangle{
	/* Instance Variables */
	private final Point top_left;
	private final Point bottom_right;

	/* Constrictors */
	public Rectangle(Point top_left, Point bottom_right){
		this.top_left = top_left;
		this.bottom_right = bottom_right;
	}

	/* Getter Methods */
	public Point getTopLeft(){
		return top_left;
	}

	public Point getBottomRight(){
		return bottom_right;
	}

	public double perimeter(){
		Point left = this.getTopLeft();
		double x = left.getX();
		double y = left.getY();

		Point right = this.getBottomRight();
		double x2 = right.getX();
		double y2 = right.getY();

		double x_units = java.lang.Math.abs(x2-x);
		double y_units = java.lang.Math.abs(y2-y);

		return((2 * x_units) + (2 * y_units));
		
	}
}


