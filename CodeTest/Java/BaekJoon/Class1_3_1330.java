package java_testPackage;

import java.util.Scanner;

public class Class1_3_1330 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		//삼항연산자 이용
		System.out.println((a>b)?">":(a<b)?"<":"==");
	}
}
