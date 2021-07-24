package java_testPackage;

import java.io.IOException;

public class Class1_19_1157 {

	public static void main(String[] args) throws IOException {
		int[] a = new int[26];
		int c, max = 0, maxa = -2;
		
		//한글자씩 읽는데, 한글자 아스키 코드값이 'a' 보다 큰 경우 반복
		while ((c = System.in.read()) > 64) {
			c -= 'a';
			if (c < 0)
				c += 32;

			a[c]++;
			
			if (max < a[c]) {
				max = a[c];
				maxa = c;
			} else if (max == a[c])
				maxa = -2;
		}
		System.out.print((char)(maxa + 65));
	}
}


/*
package java_testPackage;

import java.util.Scanner;

public class Class1_19_1157 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int arr[] = new int[26];
		int max_count = -1, max_index = -1;
		boolean sign = false;
		
		//전부 소문자로 변형
		str = str.toLowerCase();
		
		for(int i=0; i<str.length(); i++) {
			arr[str.charAt(i)-97] += 1;
		}
		
		for(int j=0; j<arr.length; j++) {
			if(max_count < arr[j]) {
				max_count = arr[j];
				max_index = j;
				sign = false;
			} else if (max_count == arr[j]) {
				sign = true;
			}
		}
		
		if(sign == true) {
			System.out.println("?");
		} else {
			System.out.println((char)(max_index+65));
		}
	}
}
*/