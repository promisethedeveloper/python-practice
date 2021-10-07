def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    # Create an empty list to save the number
    output = []
    # Loop through all elements on the list
    for num in nums:
        # Multiply all elements by 3
        num = num * 3
        # if element is divisible by 4
        if num % 4 == 0:
            # add the element to the end of the list
            output.append(num)

    return output

    # return [num * 3 for num in nums if num % 4 == 0]
