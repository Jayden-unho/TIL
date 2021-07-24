package java_testPackage;

import java.util.Scanner;

public class Class1_13_2908 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num1_changed = 0 , num2_changed = 0;
		
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		
		for(int i=2; i>-1; i--) {
			num1_changed += (int) (num1%10 * (Math.pow(10, i)));
			num2_changed += (int) (num2%10 * (Math.pow(10, i)));
			
			num1 = (int)num1/10;
			num2 = (int)num2/10;
		}
		
		//Math클래스에서 두수의 큰수 비교 가능
		System.out.println(Math.max(num1_changed, num2_changed));
		//System.out.println((num1_changed>num2_changed)?num1_changed:num2_changed);
	}
}
