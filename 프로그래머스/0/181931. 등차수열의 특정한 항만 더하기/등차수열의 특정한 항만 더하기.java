class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int n = included.length;
        for(int i = 0; i < n; i++) {
            answer += (included[i] == true) ? (a + d * i) : 0;
        }
        return answer;
    }
}