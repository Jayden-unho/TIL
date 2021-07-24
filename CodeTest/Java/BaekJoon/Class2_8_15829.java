import java.util.Scanner;
import java.lang.Math;

public class Class2_8_15829 {
    final static long M = 1234567891;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int answer = 0;
        int l = sc.nextInt();
        String input_str = sc.next();
        
        //아스키코드 값  a-97 / z-122
        for(int i=0; i<input_str.length(); i++) {
            char c = input_str.charAt(i);
            answer += ((int)c - 96) * Math.pow(31, i); 
        }

        System.out.println(answer%M);
    }
}
