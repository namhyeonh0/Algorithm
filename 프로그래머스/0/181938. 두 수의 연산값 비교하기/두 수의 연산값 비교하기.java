class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int pow = 0;
        for(int i = 0; i < 4; i++){
            if(b >= Math.pow(10,i) && b < Math.pow(10,i+1)) pow = i+1;
        }
        int AB = (int)(a*Math.pow(10,pow)) + b;
        int ab2 = a*b*2;
        return Math.max(AB,ab2);
    }
}