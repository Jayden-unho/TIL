package java_testPackage;

import java.util.ArrayList;
import java.util.Scanner;

public class Class1_7_10818 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList arr = new ArrayList();
		int n = sc.nextInt();
		
		for(int i=0; i<n; i++) {
			arr.add(sc.nextInt());
		}
		
		arr.sort(null);
		System.out.println(arr.get(0) + " " +arr.get(n-1));
	}

}

/*
package java_testPackage;

import java.util.Arrays;
import java.util.Scanner;

public class Class1_7_10818 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int arr[] = new int[n];
		
		for(int i=0; i<n; i++) {
			arr[i] = sc.nextInt();
		}
		
		//Á¤·Ä
		Arrays.sort(arr);
		System.out.println(arr[0] + " " + arr[n-1]);
	}

}
*/