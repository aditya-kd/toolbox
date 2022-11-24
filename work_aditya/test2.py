# Python3 code to demonstrate
# numeric string sorting
# using sorted() + key

# initializing list
test_list = [ '4', '6', '7', '2', '1', '']

# printing original list
print ("The original list is : " + str(test_list))

# using sorted() + key
# numeric string sorting
res = sorted(test_list, key = int)

# printing result
print ("The resultant sorted list : " + str(res))
