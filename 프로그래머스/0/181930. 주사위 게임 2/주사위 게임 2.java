import java.util.HashSet;

class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        HashSet<Integer> diceSet = new HashSet<>();
        diceSet.add(a);
        diceSet.add(b);
        diceSet.add(c);
        int size = diceSet.size();
        if(size == 1) {
            answer = (a + b +c)*(a*a + b*b + c*c)*(a*a*a + b*b*b + c*c*c);
        } else if(size == 2) {
            answer = (a + b +c)*(a*a + b*b + c*c);
        } else {
            answer = a + b + c;
        }
        
        
        return answer;
    }
}