import java.util.Scanner;

public class Class2_3_10250 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		
		for(int i=0; i<testCase; i++) {
			int answer = 0;
			int h = sc.nextInt();
			int w = sc.nextInt();
			int n = sc.nextInt();
			
			if(n%h == 0) {
				answer = h*100 + (int)n/h;
			} else {
				answer = (n%h)*100 + (int)n/h + 1;
			}
			
			System.out.println(answer);
		}
		
	}
}