import numpy as np
#时间复杂度最好O(nlogn)最坏O(n^2),平均O(nlogn)
def quicksort(array):
    if len(array)<2:
        return array
    else:
        base=array[0]
        less=[l for l in array[1:] if l < base]
        equal=[e for e in array if e==base]
        greater=[g for g in array[1:] if g>base]
    return quicksort(less)+equal+quicksort(greater)

if __name__=='__main__':
    ar=np.array([11,4,32,45,4,5,8,9])
    s = quicksort(ar)
    print(s)