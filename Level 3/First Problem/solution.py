# Function to calculate the multiplier based on the difference between two values
def multiplier(a, b):
    diff = a - b
    return (diff / b) + 1

# Main solution function with anonymous variable names
def solution(x, y):
    # Initialize variables for steps and input values
    step, m_val, f_val = 0, int(x), int(y)

    # Main loop to perform the solution logic
    while True:
        # Check if either value becomes non-positive
        if m_val <= 0 or f_val <= 0:
            break

        # Check if values are greater than 100
        if m_val > 100 or f_val > 100:
            # Handle cases where one value is greater than the other
            if m_val > f_val:
                mul = multiplier(m_val, f_val)
                m_val -= f_val * mul
                step += mul
            elif f_val > m_val:
                mul = multiplier(f_val, m_val)
                f_val -= m_val * mul
                step += mul
            else:
                # Values are equal, break the loop
                break
        else:
            # Handle cases where values are less than or equal to 100
            if m_val > f_val:
                m_val -= f_val
            elif f_val > m_val:
                f_val -= m_val
            else:
                # Values are equal, break the loop
                break
            step += 1
    
    # Check if the final condition is met, and return the result accordingly
    if m_val == 1 and f_val == 1 and step >= 0:
        return str(step)
    return 'impossible'

# # Main execution when the script is run
# if _name_ == "_main_":
#     # Test cases
#     m1, f1 = '2', '1'
#     print(anonymous_solution(m1, f1))

#     m2, f2 = '4', '7'
#     print(anonymous_solution(m2, f2))
