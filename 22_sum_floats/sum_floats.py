def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    float_num = []
    for el in nums:
        if isinstance(el, float):
            float_num.append(el)

    sum = 0
    for val in float_num:
        sum = sum + val

    return sum

    # return sum([num for num in nums if isinstance(num, float)])

    
