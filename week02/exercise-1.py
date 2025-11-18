def getManyNumbers():
   result = []
   for i in range(3):
      value = getNumber(f"Give me {i+1}: ")
      result.append(value)
   return result
      

def getNumber(message):
   flag = True
   while flag==True:
      val_str = input(message)

      try:
         val_int = int(val_str)
      except:
         continue
      flag=False
   return val_int

def getMax(numbers_list):
   max_val = numbers_list[0]
   for value in numbers_list:
      if value > max_val:
         max_val = value
   return max_val

numbers_list = getManyNumbers()
max_number = getMax(numbers_list)
print(f"The max of {numbers_list} is {max_number}")




