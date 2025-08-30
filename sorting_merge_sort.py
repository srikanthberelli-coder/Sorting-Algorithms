def merge_sort(arr):
  if len(arr)<=1:
    return arr
  # 1. Divide
  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  
  # 2. Merge
  return merge(left,right)

def merge(left,right):
  result = []
  i = j =0
  
  # compare and merge
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j +=1
  # add remaining elements
  result.extend(left[i:])
  result.extend(right[j:])
  return result

arr = [38,27,43,3,9,82,40]
print(merge_sort(arr))