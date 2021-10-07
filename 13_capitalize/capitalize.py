def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    txt = phrase.capitalize()
    return txt

    # or, doing it by hand:
    # return phrase[:1].upper() + phrase[1:]


    
    

