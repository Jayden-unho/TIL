import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Class2_13_1018 {
    public static int[][] arr;
    public static int min_change = 64;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int height = Integer.parseInt(st.nextToken());
        int width = Integer.parseInt(st.nextToken());

        arr = new int[height][width];
        for(int i=0; i<height; i++) {
            String oneLine = br.readLine();
            for(int j=0; j<width; j++) {
                //흰색이면 1, 검정이면 0
                if(oneLine.charAt(j) == 'W') {
                    arr[i][j] = 1;
                } else {
                    arr[i][j] = 0;
                }
            }
        }

        for(int a=0; a<height-7; a++) {
            for(int i=0; i<width-7; i++){
                int idx1 = 0;
                int idx2 = 0;

                for(int b=a; b<a+8; b++){
                    for(int j=i; j<i+8; j++){
                        if((j+b)%2 == 0){
                            if(arr[b][j] != 1){idx1 += 1;}
                            if(arr[b][j] != 0){idx2 += 1;}
                        } else {
                            if(arr[b][j] != 0){idx1 += 1;}
                            if(arr[b][j] != 1){idx2 += 1;}
                        }
                    }
                }

                if(min_change > idx1){min_change = idx1;}
                if(min_change > idx2){min_change = idx2;}
            }
        }        

        System.out.println(min_change);
    }
}