

def printN(n) :
    if n == 0 :
        return 
    print(n , end = " ")
    printN(n - 1)

def firstOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1 
    if nums[i] == element : 
        return i
    return firstOccurrence(nums, element ,i + 1)

def lastOccurrence(nums, element, i) :
    if i == len(nums) :
        return -1 
    if nums[i] == element : 
        ans = lastOccurrence(nums, element , i + 1)
        if ans != -1 : 
            return ans 
        else :
            return i
    return lastOccurrence(nums, element ,i + 1)

def lastOccurrence1(nums, element, i, ansSoFar) :
    if i == len(nums) :
        return ansSoFar
    if nums[i] == element : 
        ansSoFar = i
    return lastOccurrence(nums, element ,i + 1)
    
nums = [10, 10, 10, 10]

print(lastOccurrence1(nums, 10, 0, -1))

# printN(n)


"""
class Student : 
    count = 1
    def __init__(self, name, department) :
        self.name = name 
        self.department = department
        self.rollNumber = Student.count 
        Student.count += 1
    
    def printStudent(self) :
        print("Name : " , self.name, " Department : ", self.department, " Roll Number : ", self.rollNumber)
    
s = Student("abc", "cse")
s.printStudent()
s.name = "rtfuygihojpk"
s1 = Student("def", "cse")
s1.printStudent()
# print(s.name)


# print("s : ", s)
# s1 = Student("abc", "cse")
# print("s1 : ", s1)
# s.printStudent()
"""

# nums = (10, 20, 30, 40, 10)
# # nums[10] = 67   # Tuples are immutable, -> Raises TypeError
# print(nums[0])  # Read elemnent at index 0

# print(nums.index(10))   # Returns the first occurrence of value, if not present -> Raises ValueError

# print(nums , type(nums))


# nums = {
#     9 : 1, 
#     12 : 4, 
#     15 : 6 
# }

# if 45 in nums :
#     print("Present")
# else :
#     print("Not present")

# for i in nums : 
#     print(i, nums[i])

# nums[70] = 9    # Adds key value pair to dictionary.
# print(nums[9])  # Prints the value of key if present, else -> KeyError

# print(nums)



# nums = set()    # Creates an empty set
# # print(type(nums))

# nums.add(10)

# if 10 in nums : 
#     print("Yes")
# else :
    # print("No")

# for i in nums :
#     print(i, end = " ")

# nums.discard(100) # If element is not present -> No Error, else element will be removed from set -> TC -> O(1)

# nums.remove(100)    # If element is not present -> Raises KeyError, else element will be removed from set -> TC -> O(1)
# nums.add(60) # Adds element into set if it's not present, if present -> ignore -> TC -> O(1)
# print(nums, type(nums))


"""
def a() :
    print("Inside a ")

def inner() :
    a()
    print("Inside inner")

def outer() : 
    inner() 
    print("Inside outer")

outer() 
print("Inside main")
inner()
"""

# nums = [10, 90, 50, 24, 45]
# # TC -> O(n)
# if 45 in nums :
#     print("Yes")
# else :
#     print("No")

# for i in nums : 
#     print(i, end = " ")

# for i in range(len(nums)) : 
#     print(i, " ", nums[i])

# nums.pop() # Removes the last element, if not present -> Raises IndexError -> TC -> O(1)

# print(nums.index(100))  # Returns the first occurence of element, if not present -> ValueError -> TC -> O(n)

# print(nums.count(100)) # Returns a int -> counts the number of occurrences of an element -> TC -> O(n)

# print(help(nums))

# nums.append(90)  # Appends element to last -> TC -> O(1)
# nums.insert(10, 29)  # Inserts element at index -> if index is not valid -> inserts at last -> TC -> O(n)
# print(nums)

# print(nums[90]) -> IndexError -> index out of range
# print(nums[-1]) # Returns last element in list

# print(nums[0 : 4])  # Returns a sub list, start -> inclusive, end -> exclusive

"""
n = int(input("Enter n : "))
# Number pattern
end = (2 * n) - 1
for i in range(n) :
    num = (2 * i) + 1
    for j in range(n) :
        print(num, end = " ")
        num += 2
        if num > end :
            num = 1
    print()
"""

'''
# Diamond pattern

# for i in range(1, n + 1) :
#     print("_" * (n - i), end = "")
#     print("*" * ((2 * i) - 1))

# First half
for i in range(1, n + 1) : 
    # Spaces -> n - i
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i) :
        print("*", end = " ")
    print()
# Second half
for i in range(n - 1, 0, -1) : 
    # Spaces -> n - i
    for j in range(1, n - i + 1) :
        print("_", end = " ")
    # Stars -> 2 * i - 1
    for j in range(1, 2 * i) :
        print("*", end = " ")
    print()
'''

'''
a = 10
print(a, type(a))
a = 10.5
print(a,  type(a))
a = [10,20.4,[9,8,5]]
print(a[2][0],  type(a[2][0]))
'''
