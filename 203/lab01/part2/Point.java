public class Point{
	/* instance variables - the data */
	private final double x_value;
	private final double y_value;

	/* Constrictor */
	public Point(double x, double y){
		this.x_value = x;
		this.y_value = y;
	}


	/* Functions aka Method */

	public double getX(){
		return x_value;
	}

	public double getY(){
		return y_value;
	}

	public double getAngle(){
		double angle = Math.atan2(y_value, x_value);
		return angle;
	}

	public double getRadius(){
		double radius = Math.sqrt(x_value * x_value + y_value * y_value);
		return radius;
	}


	public Point rotate90(){
		double new_y;
		double new_x;

		new_y = x_value;
		new_x = (y_value * -1);

		Point newPoint = new Point(new_x, new_y);
		return newPoint;

	}

}