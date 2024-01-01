def solution(xs):
    if not xs:
        return "0"
    
    positive_numbers = [num for num in xs if num > 0]
    negative_numbers = [num for num in xs if num < 0]

    if len(negative_numbers) % 2 != 0:
        negative_numbers.remove(max(negative_numbers))

    if not positive_numbers and not negative_numbers:
        return str(xs[0])
    
    result = 1
    for num in positive_numbers + negative_numbers:
        result *= num

    return str(result)
