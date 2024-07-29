class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
        int len = section.length;
        boolean[] check = new boolean[len];
        
        for (int i = 0; i < len; i++) {
            if (check[i] == false) {
                int endIndex = section[i] + m - 1;
                answer++;
                for (int j = i; j < len; j++) {
                    if (section[j] <= endIndex) check[j] = true;
                    else break;
                }
            }
        }
        return answer;
    }
}