import java.util.*;

public class D1_2056 {
    final static int[] MONTH_DAY = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();

        String year, month, day;

        for(int i=1; i<=testCase; i++) {
            String str = sc.next();
            year = str.substring(0, 4);
            month = str.substring(4, 6);
            day = str.substring(6, 8);

            if(Integer.parseInt(month)>12 || month.equals("00")) {
                year = "-1";
            }

            if(!year.equals("-1") && (MONTH_DAY[Integer.parseInt(month)] < Integer.parseInt(day) || day.equals("00"))) {
                year = "-1";
            }

            if(year.equals("-1")) {
                System.out.println("#" + i + " " + year);
            } else {
                System.out.println("#" + i + " " + year + "/" + month + "/" + day);
            }
        }
    } 
}
