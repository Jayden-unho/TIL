package java_testPackage;

import java.util.Scanner;

public class Class1_4_2753 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int year = sc.nextInt();
		int sign = 0;
		
		if(year%4 == 0 && year%100 != 0 || year%400 == 0) {
			sign = 1;
		}
		
		System.out.println(sign);
	}
}
