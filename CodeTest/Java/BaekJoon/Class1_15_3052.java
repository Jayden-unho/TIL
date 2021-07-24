package java_testPackage;

import java.util.HashSet;
import java.util.Scanner;

public class Class1_15_3052 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//HashSet - Set(집합) 클래스 선언
		HashSet arr_set = new HashSet();
		
		for(int i=0; i<10; i++) {
			arr_set.add(sc.nextInt()%42);
		}
		
		System.out.println(arr_set.size());
	}

}
