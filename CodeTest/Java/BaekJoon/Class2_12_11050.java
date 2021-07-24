import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.io.InputStreamReader;


public class Class2_12_11050 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        double n = Double.parseDouble(st.nextToken());
        double k = Double.parseDouble(st.nextToken());
        double answer = 1;

        // 조합 combination 구현해야함
        // nCk = n!/(k!*(n-k)!)
        for(int i=1;i<n+1;i++) {
            answer *= i;

            if(i<=k) {answer /= i;}
            if(i<=(n-k)) {answer /= i;}
        }
        int int_answer = (int)answer;
        
        if(answer-int_answer == 0) {System.out.println(int_answer);}
        else if(answer-int_answer < 0.5) {System.out.println(int_answer);}
        else if(answer-int_answer > 0.5) {System.out.println(int_answer+1);}
    }
}