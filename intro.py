#PYTHON BUILD IN DATA STRUCTURES

'''
Strings, List, Tuples, Sets, Dictionary

Sequence type are : String, List, Tuple
'''

'''
Documentation
-------------

Indexing : access any item in the sequence using its index 
indexing starts with 0 for the first element
'''
# we can access any item in the sequence by using index

#string
x = 'frog'
print(x[3])

#list
x = ['pig', 'cow', 'horse']
print(x[1])

# tuple
x = ('kevin', 'Niklas', 'Jenny', 'Graig')
print(x[2])

# slicing : slice out substring, sublists, subtuples using indexes.
#[start: end+1 : step]

x = 'computer'
print(x[1:4]) # omp
print(x[1:6:2]) # opt jump 1
print(x[3:])# puter
print(x[:5]) # compu
print(x[-1]) # r
print(x[-3:]) #ter
print(x[:-2])#comput