package java_testPackage;

import java.util.Scanner;

public class Class1_14_2920 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int pre = sc.nextInt();
		String sign = "mixed";
		
		for (int i=1; i<8; i++) {
			int num = sc.nextInt();
			
			if(pre+1 == num || pre-1 == num) {
				pre = num;
				
				if(i == 7 && num == 8) {
					sign = "ascending";
				} else if(i==7 && num == 1) {
					sign = "descending";
				}
			} else {
				break;
			}
		}
		
		System.out.println(sign);		
	}

}
