
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        StringBuilder word = new StringBuilder();
        StringBuilder result = new StringBuilder();

        // 태그 안에 있는지 확인하는 플래그
        boolean inTag = false; 

        for (char c : br.readLine().toCharArray()) {

            if (c == '<') {
                inTag = true;
                // 태그가 시작되면 그동안 쌓인 단어를 뒤집어서 결과에 추가
                result.append(word.reverse());
                word.setLength(0);
                result.append(c);
            } else if (c == '>') {
                inTag = false;
                result.append(c);
            } else if (inTag) {
                // 태그 안에서는 그대로 추가
                result.append(c);
            } else {
                // 태그 밖일 때
                if (c == ' ') {
                    // 공백을 만나면 단어를 뒤집어 추가하고 공백도 추가
                    result.append(word.reverse());
                    result.append(c);
                    word.setLength(0);
                } else {
                    // 단어의 일부라면 뒤집기 위해 임시 보관
                    word.append(c);
                }
            }
        }
        // 마지막에 남은 단어 처리
        result.append(word.reverse());

        System.out.println(result);
    }
}