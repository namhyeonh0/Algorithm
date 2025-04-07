class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        
        int str1Len = str1.length();
        int str2Len = str2.length();
        
        for (int i = 0; i < str2Len - str1Len + 1; i++) {
            if (str1.equals(str2.substring(i, i + str1Len))) {
                answer = 1;
                break;
            }
        }
        
        return answer;
    }
}