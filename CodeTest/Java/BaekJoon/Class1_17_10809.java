package java_testPackage;

import java.util.Scanner;

public class Class1_17_10809 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		
		//�ƽ�Ű�ڵ尪 97-a, 122-z
		//indexOf() - ���ڿ��� ���� ������ �ε��� ��ȣ�� ����, ������ -1 ���� 
		for(int i=97; i<123; i++) {
			System.out.print(str.indexOf((char)i) + " " );
		}
	}

}
