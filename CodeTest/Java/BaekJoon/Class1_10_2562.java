package java_testPackage;

import java.util.Scanner;

public class Class1_10_2562 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int max_num = -1;
		int index = -1;
		
		for(int i=1; i<10; i++) {
			int num = sc.nextInt();
			if(num > max_num) {
				max_num = num;
				index = i;
			}
		}
		
		System.out.println(max_num + "\n" + index);
	}
}
