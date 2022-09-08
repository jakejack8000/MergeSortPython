numbers = [5,2,3,7,4,6,9,8]
def mergeSort(arr):
    print(arr)
    if len(arr)==1:
        return arr[0]
    else:
        split_point = int(len(arr)/2)
        left_half = arr[:split_point]
        left_half = mergeSort(left_half)
        right_half = arr[split_point:]
        right_half = mergeSort(right_half)
        return merge(left_half,right_half)
 
def merge(left_half,right_half):
    sorted_array = []
    if (type(left_half)==int):
        left_half = [left_half]
        right_half = [right_half]
    for i in range(len(left_half)*2):
        if (len(left_half)>0 and len(right_half)>0):
            if (left_half[0]<right_half[0]):
                sorted_array.append(left_half[0])
                left_half.pop(0)
            else:
                sorted_array.append(right_half[0])
                right_half.pop(0)
        else:
            if (len(left_half)>0):
                sorted_array.append(left_half[0])
                left_half.pop(0)
            if (len(right_half)>0):
                sorted_array.append(right_half[0])
                right_half.pop(0)
    print ("Sorted Array:")
    print(sorted_array)
    return (sorted_array)
