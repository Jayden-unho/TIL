import java.util.Scanner;

public class Class2_9_1259 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input_num = null;        
        String answer = null;

        while (true) {
            input_num = sc.next();
            answer = "";

            if(input_num.equals("0")) {break;}

            for(int i=0; i<input_num.length(); i++){
                answer = input_num.charAt(i) + answer;
            }

            if(input_num.equals(answer)) {System.out.println("yes");}
            else {System.out.println("no");}
        }
    }
}