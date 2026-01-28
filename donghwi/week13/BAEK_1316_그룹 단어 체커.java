import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = 0;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            boolean tf = true;
            String str = "";
            char[] spell = br.readLine().toCharArray();
            for (int j = 0; j < spell.length-1; j++) {
                if (spell[j] != spell[j + 1]) {
                    if (str.contains(Character.toString(spell[j+1]))) {
                        tf = false;
                        break;
                    }
                }
                str += spell[j];
            }
            if (tf == true) {
                count++;
            }
        }
        System.out.println(count);
    }
}