package java_testPackage;

import java.util.Scanner;

public class Class1_18_11720 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(), answer = 0;
		String num = sc.next();
		
		for(int i=0; i<n; i++) {
			answer += num.charAt(i)-48;
		}
		
		System.out.println(answer);
	}
}
