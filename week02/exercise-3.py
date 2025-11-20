def count(text, char):
   counter = 0
   for c in text:
      if c == char:
         counter = counter + 1
   return counter

def unique(text):
   if type(text) != str:
      return None
   return set(text)

def charCount(text):
   unique_letters = unique(text)
   for letter in unique_letters:
      count_int = count(text,letter)
      print(f"{letter}: {count_int}")

def charCount2(text):
   result = {}
   for letter in text:
      if letter in result:
         result[letter] = result[letter] + 1
      else:
         retuls[letter] = 1



text = "aspri petra kseksaspri"
# uniques_set = unique(text)
# print(uniques_set)

charCount(text)


