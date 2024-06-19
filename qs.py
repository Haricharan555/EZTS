'''def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] 
                           if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)'''

'''def partition(L, Low, High):
    P = L[High]
    j = Low - 1
    for i in range(Low, High):
        if L[i] <= P:
            j += 1
            L[i], L[j] = L[j], L[i]
    j += 1
    L[j], L[High] = L[High], L[j]
    return j

def quick_sort(L, Low, High):
    if Low < High:
        pi = partition(L, Low, High)
        quick_sort(L, Low, pi - 1)
        quick_sort(L, pi + 1, High)
    return

if name == "main":
    L = list(map(int, input("Enter the elements separated by space: ").split()))
    quick_sort(L, 0, len(L) - 1)
    print("Sorted Array:", L)'''