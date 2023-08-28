def odds_or_evens(is_even, num_list):
    if is_even:
        return [num for num in num_list if num % 2 == 0]
    else:
        return [num for num in num_list if num % 2 != 0]
