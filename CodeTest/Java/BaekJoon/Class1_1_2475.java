import java.util.Scanner;

public class Class1_1_2475 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int sum = 0;
		
		for(int i=0; i<5; i++) {
			//Math.pow(int a, int b) - a^b 을 구해줌
			sum += Math.pow(sc.nextInt(), 2);
		}
		
		System.out.println(sum%10);
	}
}
