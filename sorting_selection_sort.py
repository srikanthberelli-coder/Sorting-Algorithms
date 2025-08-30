def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_num = i
    for j in range(i+1,n):
      if arr[j] < arr[min_num]:
        min_num = j
    arr[i],arr[min_num] = arr[min_num],arr[i]
  return arr

arr = [64,25,12,22,11]
print(selection_sort(arr))