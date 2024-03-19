import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

def say_hello():
  print("Hello, world")
def quicksort_string(input_string):
    # Chuyển chuỗi đầu vào thành một mảng các số nguyên
    arr = list(map(int, input_string.split()))

    # Hàm quicksort
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)
    
    # Sử dụng hàm quicksort để sắp xếp mảng và chuyển kết quả thành chuỗi
    sorted_array = quicksort(arr)
    sorted_string = ' '.join(map(str, sorted_array))
    return sorted_string

def ptsum(a, b):
  return a+b