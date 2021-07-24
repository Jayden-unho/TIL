import java.util.Scanner;
import java.lang.Math;

public class D2_1945 {
    public static int in_num;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();

        for(int i=1; i<=testCase; i++) {
            in_num = sc.nextInt();
            
            System.out.print("#" + i);

            System.out.print(" " + search(2));
            System.out.print(" " + search(3));
            System.out.print(" " + search(5));
            System.out.print(" " + search(7));
            System.out.println(" " + search(11));
        }
    }

    public static int search(int below) {
        int a = 0;
        while ((in_num % Math.pow(below, a)) == 0) {
            a += 1;
        }
        return a-1;
    }
}