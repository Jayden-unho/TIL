package java_testPackage;

import java.util.Scanner;

public class Class1_16_8958 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int testCase = sc.nextInt();
		
		for(int i=0; i<testCase; i++) {
			String str = sc.next();
			int score = 0, answer = 0;
			
			for(int j=0; j<str.length(); j++) {
				if(str.charAt(j) == 'O') {
					score += 1;
					answer += score;
				} else {
					score = 0;
				}
			}
			System.out.println(answer);
		}
	}
}
