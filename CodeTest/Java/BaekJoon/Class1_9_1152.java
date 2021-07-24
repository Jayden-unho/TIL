package java_testPackage;

import java.util.ArrayList;
import java.util.Scanner;

public class Class1_9_1152 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList arr = new ArrayList();
		
		while(sc.hasNext()) {
			arr.add(sc.next());
		}
		System.out.println(arr.size());
	}
}
