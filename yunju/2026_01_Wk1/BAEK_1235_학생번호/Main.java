// 학생 번호
// 학생들의 번호가 주어 졌을 때 뒤에서 k자리만을 추려서 남겨 놓았을 때
// 모든 학생들 번호가 다른 최소의 k값

// 1번 아이디어
// N개의 번호. k를 1씩 늘리며 집합 생성
// 집합의 원소 개수가 N과 같다면 그 때 k값이 최소
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

// 파이썬에서 set 자바에서 HashSet으로 중복 제거
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<String> numbers = new ArrayList<>();

        for (int i=0; i<N; i++) {
            String num = br.readLine();
            numbers.add(num);
        }

        int len = numbers.get(0).length();

        for (int k=1; k<=len; k++) {
            Set<String> uniqueNums = new HashSet<>();
            for (String number : numbers) {
                uniqueNums.add(number.substring(len-k,len));
                // uniqueNums.add(number.substring(len-k));
            }
            if (uniqueNums.size() == N) {
                System.out.println(k);
                return;
            }
        }
    }
}

// 피드백
// HashSet의 add() 메서드는 데이터가 잘 들어갔으면 true, 이미 있는 데이터면 false를 반환함
// Set<String> tempSet = new HashSet<>();
// boolean isPossible = true;
// if (!tempSet.add(sub)) {isPossible=false; break;} 
// 위 방식으로 중복된 번호 발견 시 바로 다음 k 값으로 넘어가는 방식으로 가지치기 가능