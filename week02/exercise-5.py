filename='source.csv'

with open(filename,'r') as file:
   sum = 0
   count = 0
   # print(file.readline())
   for line in file.readlines():
      nonewline = line[0:-1]
      #print(nonewline)
      columns_lst = nonewline.split(',')
      for element_str in columns_lst:
         if element_str is '':
            continue
         # print(f"element_str: ({element_str})")
         element_number = float(element_str)
         sum = sum + element_number
         count = count + 1 
 #     print(line)
print(sum/count)
