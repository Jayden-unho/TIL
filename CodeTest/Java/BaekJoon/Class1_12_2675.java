package java_testPackage;

import java.util.Scanner;

public class Class1_12_2675 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		
		for(int i=0; i<testCase; i++) {
			String answer = "";
			int r = sc.nextInt();
			String s = sc.next();
			
			for(int j=0; j<s.length(); j++) {
				for(int k=0; k<r; k++) {
					answer += s.charAt(j);
				}
			}
			System.out.println(answer);
		}
		
	}

}
