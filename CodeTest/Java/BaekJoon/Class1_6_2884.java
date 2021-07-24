package java_testPackage;

import java.util.Scanner;

public class Class1_6_2884 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int hour = sc.nextInt();
		int minute = sc.nextInt();
		
		if (minute - 45 >= 0) {
			minute -= 45;
		} else {
			hour -= 1;
			minute += 15;
			if(hour < 0) {
				hour = 23;
			}
		}
		
		System.out.println(hour + " " + minute);
	}
}
