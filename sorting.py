arr = [ 12,24,35,45,46,6,66,356]
def bouble_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr):
        for j in range(len(arr) -1)):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                print(arr)
        return arr

# now election shorting 
# in this we can compair the index toother and swap the index 

def selection_sorting(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        index = i
        for j in range(i+1,len(arr) ):
            if arr[j] < arr[index] :
                arr[j] , arr[index] = arr[index] , arr[j]
                print(arr)
    return arr

# now divid and conqure by marge sort
# first we divid the list then 
# conqure and make the final result 

def marge_sort(arr):
    if len(arr) <=1 :
        return arr

    mid = len(arr) // 2

    left  = arr[:mid]
    right = arr[mid:]

    left = marge_sort(left)
    right = marge_sort(right)

    result = []
    i  , j = 0,0
    while i < len(left)  and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

























