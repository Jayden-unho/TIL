import java.util.Scanner;

public class D1_2029 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        

        for(int i=1; i<=testCase; i++) {
            int in_num1 = sc.nextInt();
            int in_num2 = sc.nextInt();
            System.out.println("#" + i + " " + (int)in_num1/in_num2 + " " + in_num1%in_num2);
        }
    }    
}
