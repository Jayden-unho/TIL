import java.util.Scanner;

public class Class2_4_2231 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		for(int i=1; i<num+1; i++) {
			int sum = i;
			int k = i;
			
			while (k>0) {
				sum += k%10;
				k = (int)k/10;
			}
			
			if(sum == num) {
				System.out.println(i);
				break;
			}
			
			if(i == num) {
				System.out.println(0);
			}
		}
	}

}
