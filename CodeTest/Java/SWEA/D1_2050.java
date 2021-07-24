import java.util.Scanner;

public class D1_2050 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input_string = sc.next();
        int num;

        for(int i=0; i<input_string.length(); i++) {
            num = (int)input_string.charAt(i) - 64;
            
            if(i == input_string.length()-1) {
                System.out.println(num);
                break;
            }
            System.out.print(num + " ");
        }
    }
}