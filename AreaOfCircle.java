import java.util.Scanner;

class AreaOfCircle{
	public static void main(String[] args) {
		double radius, area; 
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the radius: ");
		radius = scan.nextDouble();
		area = Math.PI * (radius * radius);
		System.out.println("The area of this circle is: " + area);


	}
}