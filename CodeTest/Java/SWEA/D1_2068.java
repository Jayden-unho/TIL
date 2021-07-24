import java.util.*;

public class D1_2068 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testCase = sc.nextInt();
        int num;
        int max_num;

        for(int i=1; i<=testCase; i++) {
            max_num = 0;

            for(int j=0; j<10; j++) {
                num = sc.nextInt();
                
                if(max_num < num) {
                    max_num = num;
                }
            }

            System.out.println("#" + i + " " + max_num);
        }
    }
}
