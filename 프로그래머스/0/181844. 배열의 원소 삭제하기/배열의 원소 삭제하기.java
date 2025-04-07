import java.util.*;

class Solution {
    
    int[] add(int[] answer, int element) {
       int[] array = Arrays.copyOf(answer, answer.length + 1);
       array[answer.length] = element;
       return array;
    }
    
    public int[] solution(int[] arr, int[] delete_list) {
        int[] answer = {};
        
        int arrLen = arr.length;
        int delete_listLen = delete_list.length;
        
        
        for (int i = 0; i < arrLen; i++) {
            boolean included = false;
            for (int j = 0; j < delete_listLen; j++) {
                if (arr[i] == delete_list[j]) {
                    included = true;
                    break;
                }
            }
            if (included == false) {
                answer = add(answer, arr[i]);
            }
        }
        
        return answer;
    }
}