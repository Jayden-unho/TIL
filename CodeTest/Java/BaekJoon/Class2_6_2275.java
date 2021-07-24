import java.util.Scanner;

public class Class2_6_2275 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		
		for(int i=0; i<testCase; i++) {
			int k = sc.nextInt();
			int n = sc.nextInt();
			
			int li[] = new int[n+1];
			
			for(int a = 0; a < li.length; a++) {
				li[a] = 1;
			}
			
			for(int b=0; b < k+1; b++) {
				for(int c=2; c < n+1; c++) {
					li[c] = li[c] + li[c-1];
				}
			}
			
			System.out.println(li[li.length-1]);
		}
	}

}
