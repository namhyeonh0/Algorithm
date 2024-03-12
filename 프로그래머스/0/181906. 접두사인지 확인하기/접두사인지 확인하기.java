class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
    
        if (my_string.length() < is_prefix.length()){
            answer = 0;
        } else if (is_prefix.equals(my_string.substring(0,is_prefix.length()))){
            answer = 1;
        } else{
            answer = 0;
        }
        return answer;
    }
}