import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Class2_11_2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int up = Integer.parseInt(st.nextToken());
        int down = Integer.parseInt(st.nextToken());
        int high = Integer.parseInt(st.nextToken());

        int day = (int)(high-up)/(up-down);
        int sign = (high-up)%(up-down);

        if(sign == 0) {
            System.out.println(day+1);
        } else {
            System.out.println(day+2);
        }
        
        /*
        * Scanner 사용시에 입출력 소요 시간이 너무 많음
        Scanner sc = new Scanner(System.in);

        int up = sc.nextInt();
        int down = sc.nextInt();
        int high = sc.nextInt();
        int day = 0;
        int sign = 0;
                
        day = (int)(high-up)/(up-down);
        sign = (high-up)%(up-down);

        if(sign == 0) {
            System.out.println(day+1);
        } else if(sign != 0) {
            System.out.println(day+2);
        }
        */

    }
}