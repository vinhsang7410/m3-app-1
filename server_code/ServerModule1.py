import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
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

def convert_string_to_array(input_string):
    # Tách các phần tử trong chuỗi theo dấu cách và chuyển thành list
    string_list = input_string.split()
    
    # Chuyển đổi các phần tử trong list thành số nguyên
    integer_list = [int(x) for x in string_list]
    
    return integer_list

  """def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return ' '.join(map(str, quicksort(left) + middle + quicksort(right)))"""