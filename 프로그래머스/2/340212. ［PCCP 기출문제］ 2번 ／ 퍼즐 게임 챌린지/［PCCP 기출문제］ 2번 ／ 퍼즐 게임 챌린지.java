import java.util.*;

class Solution {
    int maxLevel, minLevel, mid, len;
    public int solution(int[] diffs, int[] times, long limit) {
        maxLevel = 100000;
        minLevel = 1;
        len = times.length;
        
        while (minLevel < maxLevel) {
            mid = (maxLevel + minLevel) / 2;
            long time = calculate(mid, diffs, times);
            if (time <= limit) {
                maxLevel = mid;
            } else {
                minLevel = mid+1;
            }
            // System.out.println(Map.of(minLevel, maxLevel));
        }
        return minLevel;
    }
    
    long calculate(int level, int[] diffs, int[] times) {
        long result = times[0];
        for (int i = 1; i < len; i++) {
            if (level >= diffs[i]) {
                result += times[i];
            } else {
                result += (times[i] + times[i-1]) * (diffs[i] - level) + times[i];
            }
        }
        return result;
    }
}