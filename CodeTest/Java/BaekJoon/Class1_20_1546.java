package java_testPackage;

import java.util.Scanner;

public class Class1_20_1546 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		double sum = 0, max = 0;
		
		for(int i=0; i<n; i++) {
			int num = sc.nextInt();
			sum += num;
			
			if(max < num) {
				max = num;
			}
		}
		System.out.println(sum/max*100/n);		
	}
}