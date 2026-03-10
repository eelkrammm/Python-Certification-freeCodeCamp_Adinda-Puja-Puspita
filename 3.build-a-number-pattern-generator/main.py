def number_pattern(n):
    if not isinstance(n, int): 
        return 'Argument must be an integer value.'
    if n < 1: 
        return 'Argument must be an integer greater than 0.'
    string = '' 
    for integer in range(1,n + 1):
        if integer < n: 
            string += str(integer) + ' '
        elif integer == n: 
            string += str(integer)
    return string
