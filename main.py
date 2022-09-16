""" Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? """

# If we use a nested for loop that compares each and every value:
# Time complexity: O(n^2)
# Space complexity: O(1)

# How I picture dictionaries:
# {
#  'a':1,
#  's':1,
#  'd':1,
#  'f':1,
#  'g':1,
#  'h':1,
#  'j':1 
# }


str = "asdfghjkl;'"

""" The function isUnique() stores all occurences of each new char in a dictionary. If the char already exists in dictionary, the program is executed. """
def isUnique(s):
  chars = {}
  for letter in s:
    if (letter in chars):
      return False
    else:
      chars[letter] = 1
  return True

print(isUnique(str))



""" Python's set() is a function that stores unique values only. The function isUnique2(s) inserts all letters in s into a set. Since Python's sets can only store unique values, a duplicate value would never append to the set. """
def isUnique2(s):
  return len(s) == len(set(s))
    
print(isUnique2(str))



""" An alternative method would be to convert all characters of input string into ASCII/UDF and implement a similar algorithm as used in isUnique(s). While this may seem a more accurate method, the algorithm would do the same thing but have a longer process. """
# The function ord() in Python gives the ASCII value of any character
# print(ord("A")) ==> 65 

