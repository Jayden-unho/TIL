import java.util.Scanner;

public class Class2_10_2839 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int tmp = 0;
        int answer = 5000;
        
        for(int i=0;i<=(int)num/5;i++) {
            for(int j=0;j<=(int)num/3;j++) {
                tmp = num - (i*5) - (j*3);

                if(tmp == 0 && answer>i+j) {
                    answer = i+j;
                }
            }
        }
        if(answer == 5000) {System.out.println(-1);}
        else {System.out.println(answer);}
    } 
}
