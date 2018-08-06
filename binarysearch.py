def elementSearch( lista, num ):
    '''A function that takes an ordered list of numbers and another number. 
    The function decides using binary search whether or not the given number is 
    inside the list and returns an appropriate boolean.'''
    low = 0
    high = len( lista ) - 1
    while high > low:
        mid = ( high - low ) // 2
        if num == lista[mid]:
            return True
        elif num < lista[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False        
