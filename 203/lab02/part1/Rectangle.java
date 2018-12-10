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
}

