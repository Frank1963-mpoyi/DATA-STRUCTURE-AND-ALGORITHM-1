import random

# get values within a range
under_10 = [x for x in range (10)]
#print('under_10 : ', str(under_10))
print(f"unser_10: {under_10}")


def random_value():
    under_10 = [x for x in range (10)] # range() function return sequence number from 0 to 9 
    return (f"unser_10: {under_10}")
value = random_value()
print(value)



#get values within a range
squares = [x**2 for x in under_10] #will print all the value in under_10 squares means 2times
print(f"squares: {squares}")


#get odd numbers using mod
odds = [x for x in range(10) if x % 2 == 1]
print(f"odds: {odds}")

# get multiples of 10
ten_x = [x * 10 for x in range (10)]
# print(f"tens_x: {ten_x}")
tens_x: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# b= ten_x[1]
# c = ten_x[4]
# d= b+c/2
# print(d)

#get all numbers from a string
s = "I love 2 go t0 the store 7 times a w3ek."
nums = [x for x in s if x.isnumeric()]
print('nums : ' + ''.join(nums))

#get index of a list item 
names = ['cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate (names) if v == 'Anu'] # enumerate return a key and value
print(f'index = {idx[0]}')
# the key = 2

#delete an item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)