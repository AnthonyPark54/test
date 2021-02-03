from random import randint
import time
data= []
for _ in range(100):
    data.append(randint(1,100))

# selection sort
array = data
start_time = time.time()
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index], array[i]
end_time = time.time()
print(end_time - start_time)
#print(array)


#insertion sort
array = data
start_time = time.time()
for i in range(1,len(array)):
    for j in range(i, 0, -1):
        if array[j] <array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
end_time = time.time()
print(end_time - start_time)
#print(array)


#quick sort
array = data
start_time = time.time()
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start +1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if left >right:
            array[right], array[pivot]= array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right +1, end)

quick_sort(array, 0, len(array) -1)

end_time = time.time()
print(end_time - start_time)
#print(array)


#quick sort2
array = data
start_time = time.time()
def quick_sort2(array):
    if len(array) <=1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)
arrrr = quick_sort2(array)
end_time = time.time()
print(end_time - start_time)

#counting sort
array = data
count = [0] * (max(array) +1)
for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = " ")
