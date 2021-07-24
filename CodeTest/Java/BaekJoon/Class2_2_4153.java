package java_testPackage;

import java.util.Arrays;
import java.util.Scanner;

public class Class2_2_4153 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int arr[] = new int[3];
		
		while(true) {
			for(int i=0; i<3; i++) {
				int num = sc.nextInt();
				arr[i] = num*num;
			}
			if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
				break;
			}
			
			Arrays.sort(arr);
			
			if(arr[0] + arr[1] == arr[2]) {
				System.out.println("right");
			} else {
				System.out.println("wrong");
			}
		}
 	}
}
