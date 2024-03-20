class Solution {
    public int solution(int a, int b) {
        int aPow = 0;
        int bPow = 0;
        for(int i = 0; i < 4; i++){
            if(b >= Math.pow(10,i) && b < Math.pow(10,i+1)) aPow = i+1;
            if(a >= Math.pow(10,i) && a < Math.pow(10,i+1)) bPow = i+1;
        }
        int resultAB = (int)(a*Math.pow(10,aPow)) + b;
        int resultBA = (int)(b*Math.pow(10,bPow)) + a;
        
        return Math.max(resultAB,resultBA);
    }
}