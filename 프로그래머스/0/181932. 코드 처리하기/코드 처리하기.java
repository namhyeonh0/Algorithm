class Solution {
    public String solution(String code) {
        String answer = "";
        char mode = '0';
        for(int i = 0; i < code.length(); i++) {
            if(code.charAt(i) == '1') {
                mode = (mode == '0') ? '1' : '0';
                continue;
            }
            switch (mode) {
                case '0':
                    if(i%2 == 0) answer += code.charAt(i);
                    break;
                case '1':
                    if(i%2 == 1) answer += code.charAt(i);
                    break;
            }
        }
        if(answer.length() == 0) answer = "EMPTY";
        
        return answer;
    }
}