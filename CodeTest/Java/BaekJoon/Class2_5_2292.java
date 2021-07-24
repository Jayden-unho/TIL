import java.util.Scanner;

public class Class2_5_2292 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		int i = 0;
		while (num>0) {
			if(i==0) {
				num -= 1;
				i += 1;
				continue;
			}
			
			num = num-(6*i);
			i += 1;
		}
		
		System.out.print(i);;
	}

}