import java.util.Scanner;

public class D1_2043 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int password = sc.nextInt();
        int start_num = sc.nextInt();

        System.out.println(password - start_num + 1);
    }    
}
