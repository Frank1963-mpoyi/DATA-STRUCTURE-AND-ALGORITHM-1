#if- else condition in a comprehension must come before iteration
nums = [5,3,10,18,6,7]
new_list = [x if x % 2 == 0 else 10*x for x in nums]# if modular is not 0 make times 10 otherwise leave it 
# print(f'new list: {new_list}')

#nested loop iteration for 2D list
#b is the subsets, x is the values.
a = [[1,2], [3,4]]
new_list = [x for b in a for x in b]
print(new_list)