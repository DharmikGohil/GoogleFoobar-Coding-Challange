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
