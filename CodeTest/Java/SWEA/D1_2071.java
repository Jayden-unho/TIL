import java.util.Scanner;
import java.lang.Math;

public class D1_2071 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testCase = sc.nextInt();
        double avg;
        int answer;

        for(int i=1;i<=testCase;i++) {
            avg = 0;
            
            for(int j=0;j<10;j++) {
                avg+= sc.nextInt();
            }

            answer = (int)Math.round(avg/10);

            System.out.println("#" + i + " " + answer);
        }
    }
}
