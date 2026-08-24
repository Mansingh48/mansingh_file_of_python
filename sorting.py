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
