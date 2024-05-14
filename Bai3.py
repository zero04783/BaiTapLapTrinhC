from ._anvil_designer import Form1Template
from anvil import *
import random

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  

  def insertionSort(self, arr):
      n = len(arr)  # Get the length of the array
        
      if n <= 1:
          return  # If the array has 0 or 1 element, it is already sorted, so return
  
      for i in range(1, n):  # Iterate over the array starting from the second element
          key = arr[i]  # Store the current element as the key to be inserted in the right position
          j = i-1
          while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
              arr[j+1] = arr[j]  # Shift elements to the right
              j -= 1
          arr[j+1] = key  # Insert the key in the correct position
  def btnIS_click(self, **event_args):
    input = self.txtInput.text
    isAllNumber = input.replace(" ", "")
    if(isAllNumber.isnumeric()):
      input = " ".join(input.split())
      arr = input.split(' ')
      arr = [int(numeric_string) for numeric_string in arr]
      self.insertionSort(arr)
      listToStr = ' '.join([str(elem) for elem in arr])
      self.txtResult.text = listToStr
    else:
      self.txtResult.text = "Phải nhập là một mảng số"

  def btnRandom_click(self, **event_args):
    rand_list=[]
    n=random.randint(0,20)
    for i in range(n):
        rand_list.append(random.randint(0,50))
    rand_list = ' '.join([str(elem) for elem in rand_list])
    self.txtInput.text = rand_list