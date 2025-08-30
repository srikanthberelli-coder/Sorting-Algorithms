def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[len(arr)//2]
  left = [x for x in arr if x<pivot]
  middle =[x for x in arr if x==pivot]
  right = [x for x in arr if x>pivot]
  return quick_sort(left) + middle + quick_sort(right)

arr = [5,3,8,4,2,7,1]
print("sorted:",quick_sort(arr))