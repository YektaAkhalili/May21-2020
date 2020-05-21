import java.util.Scanner;

class CentsToDollars{
	public static void main(String[] args) {
			int cent,dollar,r;
			final int conversion_rate = 100;
			Scanner scan = new Scanner(System.in);
			System.out.println("Enter cents: ");
			cent = scan.nextInt();
			r = cent % conversion_rate;
			dollar = ( cent - r ) / conversion_rate;
			System.out.println("This is " + dollar + " dollars and " + r + " cents.");

				
	}

}