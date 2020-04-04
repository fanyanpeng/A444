import java.util.Scanner;

public class HeartRateCalculation {

	public static void main(String[] args) {
		int restingHR,Age;
		Scanner scanner=new Scanner(System.in);
		System.out.println("RestingHR:");
		restingHR=scanner.nextInt();
		System.out.println("Age:");
		Age=scanner.nextInt();

		System.out.println("Intensity|TargetHeartRate\n---------|---------------");
		for(int i=55;i<=95;i=i+5){
			int answerf=0;
			answerf=(int)((((220-Age)-restingHR)*i/100.0+restingHR)+0.5);
			System.out.printf("%d%% |%dbpm\n",i,answerf);
		}

	}

}
