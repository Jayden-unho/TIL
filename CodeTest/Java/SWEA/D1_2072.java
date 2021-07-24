import java.util.*;

public class D1_2072 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testCase = sc.nextInt();
        int arr[] = new int[10];
        int sum;
        int num;

        for(int i=1;i<testCase+1;i++) {
            sum = 0;    

            for(int j=0;j<10;j++) {
                num = sc.nextInt();
                if(num%2 == 1) {
                    sum += num;
                }
            }

            System.out.println("#" + i + " " + sum);
        }
    }
}