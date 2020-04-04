import java.util.Scanner;

public class CompareNumbers {

	public static void main(String[] args) {
		Scanner in= new Scanner(System.in);
		int a,b,c;
		System.out.println("Enter the first number:");
		a=in.nextInt();
		System.out.println("Enter the second number:");
		b=in.nextInt();
		System.out.println("Enter the third number:");
		c=in.nextInt();

		if(a==b||b==c||a==c){
			System.out.println("There are same numbers.");
		}
		else if(a>b&&a>c){
			System.out.printf("The largest number is %d.",a);
		}
		else if(b>a&&b>c){
			System.out.printf("The largest number is %d.",b);
		}
		else if(c>a&&c>b){
			System.out.printf("The largest number is %d.",c);
		}
	}

}
