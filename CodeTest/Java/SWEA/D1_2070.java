import java.util.*;

public class D1_2070 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testCase = sc.nextInt();
        int num1;
        int num2;
        String sign = null;

        for(int i=1; i<=testCase; i++) {
            num1 = sc.nextInt();
            num2 = sc.nextInt();

            if(num1 > num2) {
                sign = ">";
            } else if(num1 < num2) {
                sign = "<";
            } else {
                sign = "=";
            }

            System.out.println("#" + i + " " + sign);            
        }
    }
}