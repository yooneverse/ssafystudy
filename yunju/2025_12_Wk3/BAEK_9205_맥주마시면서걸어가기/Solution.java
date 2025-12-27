import java.util.*;

class Point {
    int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
class Solution {
    public static int calDist(Point p1, Point p2) {
        return Math.abs(p1.x-p2.x) + Math.abs(p1.y-p2.y);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            Point home = new Point(sc.nextInt(), sc.nextInt());

            Point[] conv = new Point[n];

            for (int i=0; i<n; i++) {
                conv[i] = new Point(sc.nextInt(), sc.nextInt());
            }
            Point festival = new Point(sc.nextInt(), sc.nextInt());

            boolean[] visited = new boolean[n];
            Queue<Point> q = new LinkedList<>();
            q.add(home);

            boolean success = false;

            while (!q.isEmpty()) {
                Point curr = q.poll();

                if (calDist(curr, festival) <= 1000) {
                    success = true;
                    break;
                }

                for (int i=0; i<n; i++) {
                    if (!visited[i] && calDist(curr, conv[i]) <= 1000) {
                        visited[i] = true;
                        q.add(conv[i]);
                    }
                }
            }
            System.out.println(success ? "happy" : "sad");
            
        }
    }
}