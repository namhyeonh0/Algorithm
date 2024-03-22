class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String odd = "";
        String even = "";
        for(int num : num_list) {
            if(num % 2 == 0) {
                even += String.valueOf(num);
            } else {
                odd += String.valueOf(num);
            }
        }
        answer = Integer.parseInt(even) + Integer.parseInt(odd);
        return answer;
    }
}