package test2;

public class Circle_test {

	public static void main(String[] args) {
		Circle c1 = new Circle();
		System.out.println(" Radius:" + c1.getRadius());
		System.out.println(" Colour: " + c1.getColor());
		System.out.printf(" Area: %.2f%n" , c1.getArea());
		System.out.println("\t");
		
		Circle c2  = new Circle(2.5);
		System.out.println(" Radius:" + c2.getRadius());
		System.out.println(" Colour: " + c2.getColor());
		System.out.printf(" Area: %.2f%n" , c2.getArea());
		System.out.println("\t");
		
		Circle c3 = new Circle(7.1, "Purple");
		System.out.println(" Radius:" + c3.getRadius());
		System.out.println(" Colour: " + c3.getColor());
		System.out.printf(" Area: %.2f%n" , c3.getArea());
	}
}