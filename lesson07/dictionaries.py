# Dicatonaries
band = { 
    "vocals" : "Plant",
    "guitar" : "Page"
}

band2 = dict(vocals= "Plant" , guitar ="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# How to Access Item From Dictonary 
print(band["vocals"])   # Output Will be The Value  
print(band.get("guitar")) # Other Way to Use This 'git' Method 


#List All Keys
print(band.keys())

# List all Values 
print(band.values())

# list of key/values paris as tuples 

print(band.items()) # Tuples are used to store multiple items in a single variable

# Veryfy a Key Exist in Dictionary

print("guitar" in band)
print("triangle" in band)

# Change Value to Dictonary
band["vocals"] = "Coverdale" # Band '[]' for Specify
band.update({"bass": "JPJ"}) # For Change and add New Key Values 
print (band)

#Remove For Item
print(band.pop("bass")) # 'pop' for remove the value
print(band)

band["drums"] = "Bonham"
print(band)
# popitem does it removes the last thing that was added the last key values pair that was added to the dictionary - This is going to Return a  "tuple" 
print(band.popitem()) 
print(band)

# Delete Items 
band["drums"] = "Bonham"
del band["drums"]

band2.clear()
print(band2)

del band2


# Copy a Dectionary 

# band2 = band # Create a Referance
# print("Bad Cooy !")
# print(band2) 
# print(band)

# band["drums"] = "Dave"
# print(band)


band2 = band.copy() # Use copy() method
band2["drums"] = "Dave"
print("Good Copy!")
print(band)
print(band2)

# or Use the 'dict()' Constraction function
band3= dict(band)
print("Good Copy!")
print(band3)

# Nested Dictonaries( Dictonary under Dictonary )
member1 = {
    "name" : "planet",
    "instrument" : "vocals"
}
member2 = {
    "name" : "Page", # Don't Forgot to Use Comma','
    "instrument" : "guitar"

}
band = {
    "member1" : member1,
    "member" : member2
}

print(band)
print(band["member1"]["name"])

# SETS
nums = {1,2,3,4}
# We cam also create a set use to "Constraction" function

nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))


# No duplicate allowed 
nums = {1,2,2,3}
print(nums)

# True is a duplecate of One(1), False is duplecate of Zero(0)
nums = {1,True,2,False,3,4,0}
print(nums)

# Chack a Value in a Set
print(2 in nums)

# But Cannot refer to an element in the set with an index position or a key 

# Add a new element to a Set 
nums.add(8)
print(nums)

# Add elements One Set to Anotger Set 
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# You Can Use Update with lists , tuples and dictionaries , to 

# Merge two Sets to Create a New Sets 
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# Keep Only the Duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# Keep everything expect the Duplicate
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)