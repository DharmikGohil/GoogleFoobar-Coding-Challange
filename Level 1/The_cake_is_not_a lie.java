Problem Statement:

The cake is not a lie!
======================
Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("abccbaabccba")
Output:
    2

Input:
solution.solution("abcabcabcabc")
Output:
    4

-- Java cases --
Input:
Solution.solution("abccbaabccba")
Output:
    2

Input:
Solution.solution("abcabcabcabc")
Output:
    4


Solution (In java)

public class Solution {

    // Method to find the minimum repeating pattern length in a given string
    public static int solution(String s) {
        int length = s.length();  // Get the length of the input string
        
        // Iterate over all possible pattern lengths
        for (int i = 1; i <= length; i++) {
            // Check if the current length is a divisor of the total length
            if (length % i == 0) {
                boolean valid = true;

                // Check if the string repeats with the current pattern length
                for (int j = 0; j < length - i; j++) {
                    // Compare characters at current position and the position with offset i
                    if (s.charAt(j) != s.charAt(j + i)) {
                        valid = false;  // Set to false if characters don't match
                        break;
                    }
                }

                // If the pattern is valid for the entire string, return the number of repetitions
                if (valid) {
                    return length / i;
                }
            }
        }

        return 1;  // Default case, should not reach here if the input is valid
    }
}
