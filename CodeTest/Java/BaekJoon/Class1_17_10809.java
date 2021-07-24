package java_testPackage;

import java.util.Scanner;

public class Class1_17_10809 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		
		//아스키코드값 97-a, 122-z
		//indexOf() - 문자열에 문자 있으면 인덱스 번호를 리턴, 없으면 -1 리턴 
		for(int i=97; i<123; i++) {
			System.out.print(str.indexOf((char)i) + " " );
		}
	}

}
