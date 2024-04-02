import heapq

def heapsort(arr):
    result = []
    for i in range(len(arr)):
        heapq._heapify_max(arr)
        result.insert(0,arr[0])
        del arr[0]
        
    return result
    
    
arr = [54,23,11,5,66,4]

print(heapsort(arr))