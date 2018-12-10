public class Circle{
	/* Instance Variables */
	private final Point pt;
	private final double radius;

	/* Constrictors */
	public Circle(Point point, double radius){
		this.pt = point;
		this.radius = radius;
	}

	/* Getter Methods */
	public Point getCenter(){
		return pt;
	}

	public double getRadius(){
		return radius;
	}


	public double perimeter(){
	double rad = this.getRadius();
	return(2*Math.PI*rad);
	}
}
