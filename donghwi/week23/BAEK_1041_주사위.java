import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Integer.parseInt(br.readLine());
        long result = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> cube = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            cube.add(Integer.parseInt(st.nextToken()));
        }
        if (N == 0) {
            System.out.println("0");
            return;
        }
        if (N == 1) {
            Collections.sort(cube);
            for (int i = 0; i < 5; i++) {
                result += cube.get(i);
            }
            System.out.println(result);
            return;
        }
        if (cube.get(0) > cube.get(5)) { // A-F
            cube.set(0, cube.get(5));
        }
        if (cube.get(1) > cube.get(4)) { // B-E
            cube.set(1, cube.get(4));
        }
        if (cube.get(2) > cube.get(3)) { // C-D
            cube.set(2, cube.get(3));
        }
        cube.subList(3, 6).clear();
        Collections.sort(cube);
        long front = ((long) Math.pow(N, 2) * 2) * cube.get(0);
        long side = ((N * 4) * cube.get(1)) + (((N - 2) * N * 2) * cube.get(0));
        long up = (4 * cube.get(2)) + ((N - 2) * 4) * cube.get(1) + (long) Math.pow(N - 2, 2) * cube.get(0);
        result = front + side + up;
        System.out.println(result);
    }

}