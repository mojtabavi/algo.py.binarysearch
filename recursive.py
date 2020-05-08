#lets do it

import math

def rec_binarysearch(L,U,arr,x):

    arr.sort()

    
    
    if(L > U):
        return False

    mid = int((L+U)/2)
    if(x == arr[mid]):
            return True
    if(x > arr[mid]):
        return rec_binarysearch(mid + 1,U,arr,x)
    else:
        return rec_binarysearch(L,mid - 1,arr,x)
        
    
        
