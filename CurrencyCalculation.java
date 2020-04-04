import java.util.Scanner;

public class CurrencyCalculation {

	public static void main(String[] args) {
		Scanner scanner=new Scanner(System.in);
		float euros;
		float rate;
		float dollars;
		System.out.println("How many euros are you exchanging?");
		euros=scanner.nextFloat();
		System.out.println("What is the exchange rate?");
		rate=scanner.nextFloat();

		dollars=euros*rate/100;
		System.out.printf("%.2f euros at an exchange rate of %.2f is %.2f U.S. dollars.",euros,rate,dollars);

	}

}
