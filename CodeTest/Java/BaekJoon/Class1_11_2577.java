package java_testPackage;

import java.util.Scanner;

public class Class1_11_2577 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int arr[] = {0,0,0,0,0,0,0,0,0,0};
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int result = a*b*c;
		
		while(result != 0) {
			arr[result%10] += 1;
			result = (int)(result/10);
		}
		
		for(int i=0; i<10; i++) {
			System.out.println(arr[i]);
		}
	}
}
