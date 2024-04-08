# def bin_search(arr, target):
#     start_index = 0
#     end_index = len(arr)-1
#     step = 0

#     while start_index <= end_index:
#         mid_point = (end_index+start_index)//2
#         mid_item = arr[mid_point]
#         step += 1
        
#         if mid_item == target:
#             print(step)
#             return mid_point
#         elif mid_item < target:
#             start_index = mid_point+1
#         elif mid_item > target:
#             end_index = mid_point-1
#         else:
#             print(step)
#             return None
    
# print(bin_search(list(range(100)), 35))





























def bin_search(aray, target):
  start_point = 0
  end_point = len(aray)-1
  step = 0

  while start_point <= end_point:
    mid = (start_point+end_point)//2
    mid_item = aray[mid]
    step += 1

    if mid_item == target:
      print(f"Item: {target} finded in position:{mid}, by {step} steps :)")
      break
    elif mid_item > target:
      end_point = mid-1
    elif mid_item < target:
      start_point = mid+1
    else:
      print(f"Target: {target} not in list :(")
      break

bin_search([3,5,12,14,18,100], 1)   

