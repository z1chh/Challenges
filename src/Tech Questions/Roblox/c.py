def solution(numbers):
    evens = 0
    odds =  0
    for idx, num in enumerate(numbers):
        if idx & 1:
            odds += num
        else:
            evens += num
    return "even" if evens > odds else "odd" if odds > evens else "equal"