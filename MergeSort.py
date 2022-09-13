numbers = [5,2,3,7,4,6,9,8]
def mergeSort(arr):
    #print(arr)
    if len(arr)==1:
        return arr
    else:
        split_point = int(len(arr)/2)
        left_half = arr[:split_point]
        left_half = mergeSort(left_half)
        right_half = arr[split_point:]
        right_half = mergeSort(right_half)
        return merge(left_half,right_half)
 
def merge(left_half,right_half):
    sorted_array = []
    left_index = right_index = 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_array.append(left_half[left_index])
            left_index += 1
        else :
            sorted_array.append(right_half[right_index])
            right_index += 1
    if left_index < len(left_half):
        sorted_array += left_half[left_index:]
    else : 
        sorted_array += right_half[right_index:]

    return sorted_array
    #if (type(left_half)==int):
    #    left_half = [left_half]
    #    right_half = [right_half]
    #for i in range(len(left_half)*2): ## HERE THERE IS A BUG! IT SHOULD BE len(left_half)+len(right_half) as It is not guaranteed that the length of both of them equal
    #    if (len(left_half)>0 and len(right_half)>0):
    #        if (left_half[0]<right_half[0]):
    #            sorted_array.append(left_half[0])
    #            left_half.pop(0) ### POPPING FIRST ELEMENT TAKE O(n) time complexity
    #        else:
    #            sorted_array.append(right_half[0])
    #            right_half.pop(0)
    #    else:
    #        if (len(left_half)>0):
    #            sorted_array.append(left_half[0])
    #            left_half.pop(0)
    #        if (len(right_half)>0):
    #            sorted_array.append(right_half[0])
    #            right_half.pop(0)
    #print ("Sorted Array:")
    #print(sorted_array)
    #return (sorted_array)
