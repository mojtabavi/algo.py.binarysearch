#lets do it

import math

def iterative_binarysearch(L,U,arr,x):

    arr.sort()

    
    
    while(L <= U):

        mid = int((L+U)/2)
        if(x == arr[mid]):
            return True
        if(x > arr[mid]):
            L = mid + 1
        else:
            U = mid -1
        
    return False
        



    

