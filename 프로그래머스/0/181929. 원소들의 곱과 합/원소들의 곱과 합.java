class Solution {
    public int solution(int[] num_list) {
        int mul = 1;
        int add = 0;
        for(int num : num_list){
            mul *= num;
            add += num;
        }
        
        return (mul<Math.pow(add,2))?1:0;
    }
}