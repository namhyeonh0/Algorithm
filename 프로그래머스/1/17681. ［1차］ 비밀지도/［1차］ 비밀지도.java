class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        String[] ansAry = new String[n];
        //String strFormat = String.format("0%dd",n);
        
        for(var i = 0; i < n; i++){
            int ansEle = arr1[i] | arr2[i];
            String ansStr = Integer.toBinaryString(ansEle);
            ansAry[i] = ansStr;
        }
        
        for(var j = 0; j < n; j++){
            if(ansAry[j].length() == n){
                String str1 = ansAry[j].replace('0',' ').replace('1','#');
                answer[j] = str1;
            }
            else{
                ansAry[j] = "0".repeat(n - ansAry[j].length()) + ansAry[j];
                System.out.println(ansAry[j]);
                String str1 = ansAry[j].replace('0',' ').replace('1','#');
                answer[j] = str1;               
            }
        }
        return answer;
    }      
}