class Solution {
    int[] videoEnd, now, opStart, opEnd;
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        
        videoEnd = intTime(video_len);
        now = intTime(pos);
        opStart = intTime(op_start);
        opEnd = intTime(op_end);
        
        for (String command : commands) {
            opSkip();
            if (command.equals("prev")){
                if (now[1] < 10) {
                    now[0]--;
                    now[1] += 50;
                } else {
                    now[1] -= 10;
                }
                if (now[0] < 0) now = new int[]{0, 0};
            } else {
                if (now[1] > 50) {
                    now[0]++;
                    now[1] -= 50;
                } else {
                    now[1] += 10;
                }
                if (now[0] > videoEnd[0]) {
                    now[0] = videoEnd[0];
                    now[1] = videoEnd[1];
                } else if (now[0] == videoEnd[0] && now[1] > videoEnd[1]) {
                    now[0] = videoEnd[0];
                    now[1] = videoEnd[1];
                }
            }
            opSkip();
        }
        answer = (now[0] < 10 ? "0" + now[0] : now[0]) + ":" + (now[1] < 10 ? "0" + now[1] : now[1]);
        
        return answer;
    }
    
    int[] intTime(String stringTime) {
        int[] time = new int[2];
        time[0] = Integer.parseInt(stringTime.split(":")[0]);
        time[1] = Integer.parseInt(stringTime.split(":")[1]);
        return time;
    }
    
    void opSkip() {
        if (now[0] > opStart[0] && now[0] < opEnd[0]) {
            now[0] = opEnd[0];
            now[1] = opEnd[1];
        } else if (now[0] == opStart[0] && now[0] < opEnd[0] && now[1] >= opStart[1]) {
            now[0] = opEnd[0];
            now[1] = opEnd[1];
        } else if (now[0] == opEnd[0] && now[0] > opStart[0] && now[1] <= opEnd[1]) {
            now[1] = opEnd[1];
        } else if (now[0] == opStart[0] && now[0] == opEnd[0] && now[1] >= opStart[1] && now[1] <= opEnd[1]) {
            now[1] = opEnd[1];
        }
    }
}