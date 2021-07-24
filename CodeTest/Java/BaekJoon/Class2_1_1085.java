package java_testPackage;

import java.util.Scanner;

public class Class2_1_1085 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt() ,y = sc.nextInt() ,w = sc.nextInt() ,h = sc.nextInt();
		int result = Math.min(Math.min(x,y), Math.min(w-x,h-y));
		System.out.println(result);
	}
}

/*
package java_testPackage;

import java.util.Scanner;

public class Class2_1_1085 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt() ,y = sc.nextInt() ,w = sc.nextInt() ,h = sc.nextInt();
		int dis1 = (x>y)?y:x;
		int dis2 = ((w-x)>(h-y))?(h-y):(w-x);
		int result = dis1>dis2?dis2:dis1;
		
		System.out.println(result);
	}
}
*/