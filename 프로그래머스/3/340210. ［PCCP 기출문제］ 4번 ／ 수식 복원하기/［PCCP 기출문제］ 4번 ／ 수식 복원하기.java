import java.util.*;

class Solution {
    
    int num1, num2, num3;
    String operator;
    int minimum = 2;

    void findMinimumFormation() {
        int[] nums;
        if (num3 == -1) {
            nums = new int[]{num1 / 10, num1 % 10, num2 / 10, num2 % 10};
        } else {
            nums = new int[]{num1 / 10, num1 % 10, num2 / 10, num2 % 10, num3 / 100, (num3 % 100) / 10, num3 % 10};
        }
        for (int num : nums) {
            minimum = Math.max(minimum, num + 1);
        }
    }

    void findFormation(List<Integer> formation) {
        Iterator<Integer> iterator = formation.iterator();
        while (iterator.hasNext()) {
            int formationNum = iterator.next();
            int realNum1 = (num1 / 10) * formationNum + (num1 % 10);
            int realNum2 = (num2 / 10) * formationNum + (num2 % 10);
            int realNum3 = (num3 / 100) * formationNum * formationNum + ((num3 % 100) / 10) * formationNum + (num3 % 10);
            switch (operator) {
                case "+" -> {
                    if (realNum1 + realNum2 != realNum3) {
                        iterator.remove();
                    }
                }
                case "-" -> {
                    if (realNum1 - realNum2 != realNum3) {
                        iterator.remove();
                    }
                }
            }
        }
    }
    
    public String[] solution(String[] expressions) {
        String[] answer = {};
        
        List<String[]> includeX = new ArrayList<>();
        List<String[]> notIncludeX = new ArrayList<>();
        for (String expression : expressions) {
            String[] split = expression.split(" ");
            operator = split[1];
            num1 = Integer.parseInt(split[0]);
            num2 = Integer.parseInt(split[2]);
            if (split[4].equals("X")) {
                includeX.add(split);
                num3 = -1;
            } else {
                notIncludeX.add(split);
                num3 = Integer.parseInt(split[4]);
            }
            findMinimumFormation();
        }
        answer = new String[includeX.size()];

        List<Integer> formationList = new LinkedList<>();
        for (int i = minimum; i <= 9; i++) formationList.add(i);
        Iterator<Integer> iterator = formationList.iterator();
        for (String[] notIncludeXExpression : notIncludeX) {
            num1 = Integer.parseInt(notIncludeXExpression[0]);
            num2 = Integer.parseInt(notIncludeXExpression[2]);
            num3 = Integer.parseInt(notIncludeXExpression[4]);
            operator = notIncludeXExpression[1];
            findFormation(formationList);
        }

        for (int i = 0; i < includeX.size(); i++) {
            String[] includeXExpression = includeX.get(i);
            boolean onlyOneAnswer = true;
            num1 = Integer.parseInt(includeXExpression[0]);
            num2 = Integer.parseInt(includeXExpression[2]);
            num3 = -1;
            operator = includeXExpression[1];
            for (int formation : formationList) {
                int realNum1 = (num1 / 10) * formation + (num1 % 10);
                int realNum2 = (num2 / 10) * formation + (num2 % 10);
                if (num3 == -1) {
                    switch (operator) {
                        case "+" -> {
                            int realNum3 = realNum1 + realNum2;
                            num3 = Integer.parseInt(Integer.toString(realNum3, formation));
                        }
                        case "-" -> {
                            int realNum3 = realNum1 - realNum2;
                            num3 = Integer.parseInt(Integer.toString(realNum3, formation));
                        }
                    }
                } else if (onlyOneAnswer) {
                    switch (operator) {
                        case "+" -> {
                            onlyOneAnswer = num3 == Integer.parseInt(Integer.toString(realNum1 + realNum2, formation));
                        }
                        case "-" -> {
                            onlyOneAnswer = num3 == Integer.parseInt(Integer.toString(realNum1 - realNum2, formation));
                        }
                    }
                }
            }
            if (onlyOneAnswer) {
                String result = includeXExpression[0] + " " + includeXExpression[1] + " " + includeXExpression[2] + " = " + num3;
                answer[i] = result;
            } else {
                String result = includeXExpression[0] + " " + includeXExpression[1] + " " + includeXExpression[2] + " = ?";
                answer[i] = result;
            }
        }
        
        return answer;
    }
}