""" This snippet can be used to transpose a 2D array. """
array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*array)
print(transposed) # [('a', 'c', 'e'), ('b', 'd', 'f')]


""" get size of an object """
import sys 
variable = 30 
print(sys.getsizeof(variable)) # 24

""" This method returns the length of a string in bytes."""
def byte_size(string):
    return(len(string.encode('utf-8')))
byte_size('😀') # 4
byte_size('Hello World') # 11  

""" This method removes falsy values (False, None, 0 and “”) from a list by using filter(). """
def compact(lst):
    return list(filter(None, lst))
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]

""" merge dict and create dict from lists """
def merge_dictionaries(a, b):
   return {**a, **b}
a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}

print(merge_dictionaries(a, b)) # {'y': 3, 'x': 1, 'z': 4}
def to_dictionary(keys, values):
    return dict(zip(keys, values))
keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values)) # {'a': 2, 'c': 4, 'b': 3}


""" **KWARGS """
dictionary = {"a": 1, "b": 2}

def someFunction(a, b):
    print(a + b)
    return
    
# these do the same thing:
someFunction(**dictionary)
someFunction(a=1, b=2)


""" METHOD """
#title() -> captilize first letter
#shuffle(list) -> randomize list
#a, b = b, a -> swap 


