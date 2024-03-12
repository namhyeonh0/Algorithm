class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        if (num_list.length >= 11){
            int num1 = 0;
            for (int i = 0; i < num_list.length; i++){
                num1 += num_list[i];
            }
            answer = num1;
        } else{
            int num1 = 1;
            for (int i = 0; i < num_list.length; i++){
                num1 *= num_list[i];
            }
            answer = num1;
        }
        return answer;
    }
}