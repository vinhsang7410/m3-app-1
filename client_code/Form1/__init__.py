from ._anvil_designer import Form1Template
from anvil import *


class function():
  @staticmethod
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

  @staticmethod
  def merge_sort(input_string):
    # Chuyển chuỗi đầu vào thành một mảng các số nguyên
    arr = list(map(int, input_string.split()))

    # Hàm merge_sort
    def merge_sort_helper(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Đệ quy sắp xếp các nửa của mảng
        left_sorted = merge_sort_helper(left_half)
        right_sorted = merge_sort_helper(right_half)

        # Gộp hai nửa đã sắp xếp
        return merge(left_sorted, right_sorted)

    def merge(left, right):
        result = []
        left_index, right_index = 0, 0

        # Merge hai mảng đã sắp xếp
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        
        # Thêm các phần tử còn lại từ mỗi mảng
        while left_index < len(left):
            result.append(left[left_index])
            left_index += 1
        while right_index < len(right):
            result.append(right[right_index])
            right_index += 1
        
        return result
    
    # Gọi hàm merge_sort_helper để sắp xếp mảng và chuyển kết quả thành chuỗi
    sorted_array = merge_sort_helper(arr)
    sorted_string = ' '.join(map(str, sorted_array))
    return sorted_string

  @staticmethod
  def bubble_sort(input_string):
    # Chuyển chuỗi đầu vào thành một mảng các số nguyên
    arr = list(map(int, input_string.split()))

    # Hàm bubble_sort
    def bubble_sort_helper(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Gọi hàm bubble_sort_helper để sắp xếp mảng
    bubble_sort_helper(arr)
    
    # Chuyển mảng đã sắp xếp thành chuỗi
    sorted_string = ' '.join(map(str, arr))
    return sorted_string

  @staticmethod
  def selection_sort(input_string):
    # Chuyển chuỗi đầu vào thành một mảng các số nguyên
    arr = list(map(int, input_string.split()))

    # Hàm selection_sort
    def selection_sort_helper(arr):
        n = len(arr)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # Gọi hàm selection_sort_helper để sắp xếp mảng
    selection_sort_helper(arr)
    
    # Chuyển mảng đã sắp xếp thành chuỗi
    sorted_string = ' '.join(map(str, arr))
    return sorted_string
class Form1(Form1Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnSort_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.txtNumbers_QS.text = function.quicksort_string(self.txtnumber.text)
    self.txtNumbers_MS.text = function.merge_sort(self.txtnumber.text)
    self.txtNumbers_BS.text = function.bubble_sort(self.txtnumber.text)
    self.txtNumbers_SS.text = function.selection_sort(self.txtnumber.text)
    pass

  def btnSort_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass
    
  

