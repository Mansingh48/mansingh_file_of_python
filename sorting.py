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
