import java.util.Scanner;

public class Class2_7_2798 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int li[] = new int[n];
		int max_num = 0;
		int sum_num = 0;
		
		for(int i=0; i<n; i++) {
			li[i] = sc.nextInt();
		}
		
		for(int a=0; a<n-2; a++) {
			for(int b=a+1; b<n-1; b++) {
				for(int c=b+1; c<n; c++) {
					sum_num = li[a] + li[b] + li[c];
					if(sum_num <= m && max_num<sum_num) {
						max_num = sum_num;
					}
				}
			}
		}

		System.out.print(max_num);
	}

}
