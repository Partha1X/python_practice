'''This code snippet covers various operations with 
lists and tuples, along with explanations for beginners.'''


# Define a list of users
users = ['Dave', 'Joan', 'Sara']

# Create a list with mixed data types
data = ['Dave', 42, True]

# Create an empty list
emptylist = []

# Check if 'Dave' is in the emptylist (it should be False)
print("Dave" in emptylist)

# Access the first user in the 'users' list (index 0)
print(users[0])

# Access the second-to-last user in the 'users' list (negative index)
print(users[-2])

# Find the index of 'Sara' in the 'users' list
print(users.index('Sara'))

# Slice the 'users' list from index 0 to 2 (excluding 2)
print(users[0:2])

# Slice the 'users' list from index 1 to the end
print(users[1:])

# Slice the 'users' list from the third-to-last to the last element
print(users[-3:-1])

# Get the length of the 'data' list
print(len(data))

# Append 'Elsa' to the 'users' list
users.append('Elsa')
print(users)

# Extend the 'users' list with ['Jason']
users += ['Jason']
print(users)

# Extend the 'users' list with ['Robert', 'Jimmy']
users.extend(['Robert', 'Jimmy'])
print(users)

# Insert 'Bob' at the beginning of the 'users' list
users.insert(0, 'Bob')
print(users)

# Insert 'Eddie' and 'Alex' at index 2 in the 'users' list
users[2:2] = ['Eddie', 'Alex']
print(users)

# Replace elements at index 1 and 2 with 'Robart' and 'JPJ'
users[1:3] = ['Robart', 'JPJ']
print(users)

# Remove 'Bob' from the 'users' list
users.remove('Bob')
print(users)

# Remove and return the last element of the 'users' list
print(users.pop())
print(users)

# Delete the first element from the 'users' list
del users[0]
print(users)

# Clear the 'data' list
data.clear()
print(data)

# Sort the 'users' list in ascending order
users.sort()
print(users)

# Sort the 'users' list in ascending order ignoring case
users.sort(key=str.lower)
print(users)

# Create a list of numbers
nums = [4, 42, 78, 1, 5]

# Reverse the 'nums' list
nums.reverse()
print(nums)

# Sort the 'nums' list in descending order using sorted()
sorted_nums = sorted(nums, reverse=True)
print(sorted_nums)
print(nums)  # 'nums' remains unchanged

# Create copies of the 'nums' list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)  # 'nums' remains unchanged

# Check the data type of the 'nums' list
print(type(nums))

# Create a list with mixed data types
mylist = list([1, "Nell", True])
print(mylist)

# Tuples

# Create a tuple with mixed data types
mytuple = tuple(['Dave', 42, True])

# Create another tuple
anothertuple = (1, 4, 2, 8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Convert a tuple to a list, append 'Nill', and convert it back to a tuple
newlist = list(mytuple)
newlist.append('Nill')
newtuple = tuple(newlist)
print(newtuple)

# Unpack values from a tuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

# Count the number of occurrences of 2 in 'anothertuple'
print(anothertuple.count(2))
